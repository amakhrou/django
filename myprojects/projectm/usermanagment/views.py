from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreatUserForm

# Create your views here.
def home_page(request):
    context = {}
    return render(request, 'home.html')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreatUserForm()
    
        if request.method == 'POST':
          form = CreatUserForm(request.POST)
          if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account Created ' + username)
            return redirect('login')
        context = {'form':form}
        return render(request, 'register.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username Or Password incorrect')
        context = {}
        return render(request, 'login.html', context)

@login_required(login_url='login')
def logout_page(request):
  logout(request)
  return redirect('login')
