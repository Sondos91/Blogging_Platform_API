from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    bio = models.TextField(default="")  
    profile_pic = models.ImageField(upload_to="profile_pics", default="",blank=True,null=True)