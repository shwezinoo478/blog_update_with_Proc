from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse,JsonResponse
from post.models import Post,Comment,Author,Label
from django.views.generic import View
from django.core.paginator import Paginator
# Create your views here.
class HomeView(View):
    def get(self,request ):
        post = []
        if 'category' in request.GET:
            posts = Post.objects.all().filter ( label_id = request.GET['category'])
        elif 'author' in request.GET:
            posts = Post.objects.all().filter ( posted_by_id = request.GET['author'])
        elif 'q' in request.GET:
            print (Post.objects.all().filter ( title__contains = "Beauty"))
            print(request.GET['q'])
            posts = Post.objects.all().filter ( title__contains = request.GET['q'])
        else:
            posts = Post.objects.all()
        
        paginator = Paginator(posts, 3) 

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render ( request, 'post/posts_view.html' ,
        {'pages' : page_obj})  

def view_details(request , id : int):
    print (" id is =>>>>"  +str(id))
    post = Post.objects.get(pk = id)
    comment = Comment.objects.all().filter(label_id = id).order_by('commented_at')
    print(id)
    return render (request, 'post/post_detail.html' ,{'post':post , 'comments': comment})

def view_comment(request , id : int ):
    post = Post.objects.get(pk = id)
    print(" *********")
    print(request.method)
    print(request)
    if request.method == 'POST' :
        print(" comment by is " + str(request.POST['is_anonymous']))
        print(" ")
        if(request.POST['is_anonymous'] =='Anonymous'):
            is_anonymous = True
            commented_by = 'Anonymous'
        else:
            is_anonymous = False
            commented_by = request.POST['name_comment']

        print ("Is anonymous :   " +str(is_anonymous))
        description = request.POST['description'] 
        comment = Comment(
            commented_by = commented_by,
            description = description,
            label = post,
            is_anonymous = is_anonymous

        )
        comment.save()
        return redirect ('post_detail' , post.id)
    return render ( request , 'post/post_comment.html' , 
     {'post' : post}
     )


def get_categories(request):
    labels = Label.objects.all().order_by('name')
    list={}
    for label in labels:
        list[label.name] = label.pk
    return JsonResponse(list)



def get_authors(request):
    authors = Author.objects.all().order_by('display_name')
    author_list={}
    for author in authors:
        author_list[author.display_name] = author.pk
    return JsonResponse(author_list)
