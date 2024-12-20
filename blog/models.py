from django.db import models
from accounts.models import User

# Create your models here.


class Blog(models.Model):
    Title = models.CharField(max_length=100)
    Content = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Published_Date= models.DateTimeField(auto_now_add=False,null=True)
    Created_Date= models.DateTimeField(auto_now_add=True)
    Category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100)