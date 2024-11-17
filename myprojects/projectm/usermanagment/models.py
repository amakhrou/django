from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # friend = models.ManyToManyField("self", symmetrical=True, blank=True)
    firstname = models.CharField(max_length=30,default="")
    lastname = models.CharField(max_length=30,null=True, blank=True)
    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        profile_user = user_profile(user=instance)
        profile_user.save()

post_save.connect(create_profile, sender=User)