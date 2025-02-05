from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.hashers import make_password
from .models import User

def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']
            user_password1 = form.cleaned_data['user_password1']

            # Hash the password before saving it
            hashed_password = make_password(user_password1)

            User.objects.create(
                user_name=user_name,
                user_email=user_email,
                user_password1=hashed_password,
                user_password2=hashed_password

            )

            user = form.save()

            return redirect('login')  # Redirect to login after successful signup
        else:
            form = SignupForm()



    return render(request, 'signup.html')


# Create your views here.
