from django.shortcuts import render, redirect

from django.contrib.auth.hashers import make_password
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegisterForm,CustomLoginForm

def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'signup.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Redirect to the home page after successful login
    else:
        form = CustomLoginForm()

    return render(request, 'login.html',{'form':form})







# Create your views here.
