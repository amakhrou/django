from django.contrib import admin
from django.contrib.auth.models import Group
from .models import user_profile

# Register your models here.

admin.site.unregister(Group)
admin.site.register(user_profile)
