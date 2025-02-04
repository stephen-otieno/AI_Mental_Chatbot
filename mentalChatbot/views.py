from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

# Create your views here.
