from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Chat
from django.contrib.auth.forms import UserCreationForm
from .forms import CreatUserForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='first')
def chat(request):
  mychat = Chat.objects.all().values()
  template = loader.get_template('all_chat.html')
  context = {
    'mychat': mychat,
  }
  return HttpResponse(template.render(context, request))

@login_required(login_url='first')
def details(request, slug):
  mychat = Chat.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
      'mychat': mychat,
  }
  return HttpResponse(template.render(context, request))

@login_required(login_url='first')
def userProfile(request):
  user = request.user.chat
  form = UserProfileForm(instance=user)
  template = loader.get_template('userprofile.html')
  context = {
    'form':form
  } 
  # form.save()
  return HttpResponse(template.render(context, request))

# @login_required(login_url='first')
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

@login_required(login_url='first')
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'x': ['Apple', 'Banana', 'Cherry'], 
    'y': ['Apple', 'Banana', 'Cherry'], 
  }
  return HttpResponse(template.render(context, request))

def first(request):
  if request.user.is_authenticated:
      return redirect('main')
  else:
    if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = authenticate(request, username=username, password=password)
      # print(username)
      if user is not None:
        # print(username)
        login(request, user)
        return redirect('chat')
      else:
        messages.info(request, 'Username Or Password incorrect')
    context = {}
    return render(request, 'first.html', context)

def last(request):
  logout(request)
  return redirect('first')

def signup(request):
  if request.user.is_authenticated:
    return redirect('main')
  else:
    form = CreatUserForm()
  
    if request.method == 'POST':
      form = CreatUserForm(request.POST)
      if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')
        Chat.objects.create(
          user=user,
          user_mail=user.email,
          firstname=user.first_name,
          lastname=user.last_name,
          slug=user
        )
        messages.success(request, 'Account Created ' + username)
        return redirect('first')
    context = {'form':form}
    #   data = Loginform(request.POST)
    return render(request, 'signup.html', context)
