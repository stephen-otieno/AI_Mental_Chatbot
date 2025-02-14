from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.hashers import make_password
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    return render(request,'index.html')

# def signup(request):
#     form=UserCreationForm()
#
#     if request.method == 'POST':
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#
#
#     context = {'form':form}
#     return render(request,'signup.html',context)
#

# def login_page(request):
#     return render(request,'login.html')




def login_page(request):
    if request.method == 'POST':
            email = request.POST.get('user_email')
            password = request.POST.get('user_password1')


            # Authenticate user with email and password
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('homepage')  # Ensure this points to a valid route
            else:
                messages.error(request, "Invalid credentials")
                return redirect('login')




    return render(request, 'login.html')


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
