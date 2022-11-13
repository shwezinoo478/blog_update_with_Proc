from django.contrib import admin

# Register your models here.
from .models import Author 
from .models import Label
from .models import Post
from .models import Comment

admin.site.register(Label)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)