from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
#from django_mysql.models import *
#import django_mysql.models.SearchField
#from django_mysql.models. import SearchField
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
class Article(models.Model):
    author = models.ForeignKey(User,  null=False,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField()
    categories = models.ManyToManyField(Category)
    #search_vector = SearchVectorField( blank=True, null=True)

class Image(models.Model):
    author = models.ForeignKey(User, null=False,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/images/')
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    #search_vector = SearchField( blank=True, null=True)

class Video(models.Model):
    author = models.ForeignKey(User, null=False,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='media/videos/')
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    #search_vector = SearchField( blank=True, null=True)


