from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('chat/', views.chat, name='chat'),
    path('chat/details/<slug:slug>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('first/', views.first, name='first'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.last, name='logout'),
    path('userProfile/', views.userProfile, name='userProfile'),
    path('profile/', views.profile_page, name='profile')
]
