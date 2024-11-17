from django.contrib import admin
from .models import Chat
from django.contrib.auth.models import Group
# Register your models here.

class ChatAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  pre = {"slug": ("firstname", "lastname")}

admin.site.register(Chat, ChatAdmin)
admin.site.unregister(Group)

# admin.site.register(Login)
admin.site.site_title = 'aymen\'s'
admin.site.site_header = 'aymen\'s'

