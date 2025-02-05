from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.hashers import make_password
from .models import User

def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user_name = form.cleaned_data['user_name']
#             user_email = form.cleaned_data['user_email']
#             user_password1 = form.cleaned_data['user_password1']
#
#             # Hash the password before saving it
#             hashed_password = make_password(user_password1)
#
#             User.objects.create(
#                 user_name=user_name,
#                 user_email=user_email,
#                 user_password1=hashed_password,
#                 user_password2=hashed_password
#
#             )
#
#             user = form.save()
#
#             return redirect('login')  # Redirect to login after successful signup
#         else:
#             form = SignupForm()
#
#
#
#     return render(request, 'signup.html')

def signup(request):
    if request.method == 'POST':
        print("Signup form submitted")  # Debugging

        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        password1 = request.POST['user_password1']
        password2 = request.POST['user_password2']

        # Check if passwords match
        if password1 != password2:
            print("Passwords do not match")  # Debugging
            return render(request, 'signup.html', {'error': "Passwords do not match"})

        # Check if user already exists
        if User.objects.filter(user_email=user_email).exists():
            print("Email already exists")  # Debugging
            return render(request, 'signup.html', {'error': "Email already in use"})

        # Save the user
        user = User(user_name=user_name, user_email=user_email, user_password1=make_password(password1))
        user.save()

        print("User created successfully")  # Debugging
        return redirect('login')
    return render(request, 'signup.html')






# Create your views here.
