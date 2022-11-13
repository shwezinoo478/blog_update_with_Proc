from django.urls import path
from . import views as postView
urlpatterns = [

    path('', postView.HomeView.as_view(), name= "view_posts"),
    path('detail_post/<int:id>/', postView.view_details, name='post_detail'),
    path('comment_post/<int:id>/', postView.view_comment, name="post_comment"),
    path('category/', postView.get_categories ,name = "get_json_data" ),
    path('author/' , postView.get_authors , name = "get_json_author"),
    

]