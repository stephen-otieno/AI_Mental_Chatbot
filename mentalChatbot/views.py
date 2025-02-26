from boto3 import client
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.auth.hashers import make_password
from .models import Client
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



@login_required(login_url='login')
def relationships(request):
    return render(request,'relationships.html')


@login_required(login_url='login')
def drugs(request):
     return render(request,'drugs.html')

@login_required(login_url='login')
def mental_illness(request):
    if request.method == 'POST':
        client_name = request.POST['client_name']
        client_email = request.POST['client_email']
        client_message = request.POST['client_message']

        clients = Client(
            client_name=client_name,
            client_email=client_email,
            client_message=client_message

        )
        clients.save()

    return render(request, 'mental_illness.html')

@login_required(login_url='login')
def disability(request):
    return render(request, 'disability.html')




# Create your views here.
