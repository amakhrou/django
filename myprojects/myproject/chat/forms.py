from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Chat

# from .models import Login

class UserProfileForm(ModelForm):
    class Meta:
        model = Chat
        fields = '__all__'
        exclude = ['user', 'slug', 'user_mail', 'joined_date', 'phone']

class CreatUserForm(UserCreationForm):
    class Meta:
        first_name = forms.CharField(max_length=30, required=True)
        last_name = forms.CharField(max_length=30, required=True)
        model = User
        fields = ['username', 'first_name','last_name', 'email', 'password1', 'password2']