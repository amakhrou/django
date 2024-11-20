from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    user_mail = models.CharField(max_length=255,null=True)
    display_name = models.CharField(max_length=255, null=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    joined_date = models.DateField(auto_now_add=True, null=True)
    slug = models.SlugField(default="", null=False)

# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

def __str__(self):
    return f"{self.firstname} {self.lastname}"