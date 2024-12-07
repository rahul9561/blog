from django.db import models

# Create your models here.


class blog(models.Model):
    img=models.ImageField(upload_to='blogs/')
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.title
    


# from tinymce.models import HTMLField


    

from ckeditor.fields import RichTextField

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()  # CKEditor field

    def __str__(self):
        return self.title