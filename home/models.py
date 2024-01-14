from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.TextField()
    date = models.DateField()
    blog_content = models.TextField()
    

