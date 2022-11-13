from django.db import models
from django.utils import timezone
# Create your models here.
class Label(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50 , null = False , blank = False ,unique = True)
    is_active = models.BooleanField(default = "False")

    def __str__(self):
        return (self.name)

class Author(models.Model):
    gender_list = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )
    id = models.AutoField(primary_key=True)
    about_me = models.CharField(max_length=500 , null = True , blank =False)
    profile_image = models.FileField(upload_to='authors')
    display_name = models.CharField( max_length=50)
    email = models.EmailField(max_length=50 , null = False, blank = False , unique = True)
    gen5der = models.CharField(max_length=1, choices=gender_list)
    show_gender = models.BooleanField(default = "True")
    show_email = models.BooleanField(default = "True")

    def __str__(self):
        return (self.display_name)

class Post(models.Model):
    posted_at = models.DateTimeField(null = False, blank = False , default = timezone.datetime.now() )
    title = models.CharField(max_length = 255 , null = False, blank = False )
    content = models.CharField(max_length = 500 , null = False, blank = False )
    posted_by = models.ForeignKey("Author", on_delete=models.CASCADE)
    label = models.ForeignKey("Label", on_delete=models.CASCADE)
    def __str__(self):
        return (f"{self.pk} =>{self.posted_by} posted {self.title}")


class Comment(models.Model):
    commented_by = models.CharField(max_length = 50)
    commented_at = models.DateTimeField(null = False, blank = False , default=timezone.datetime.now())
    description = models.CharField(max_length = 500  )
    label = models.ForeignKey("Post", on_delete=models.CASCADE)
    is_anonymous = models.BooleanField( null = False, blank = False , default = "True")
    
    def __str__(self):
        return (f"{self.commented_by} commented {self.commented_at}" )
