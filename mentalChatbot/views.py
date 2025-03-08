from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Client, ForumPost, ForumResponse
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


@login_required(login_url='login')
def view_clients(request):
    clients = Client.objects.all()
    return render(request, 'view_clients.html', {'clients':clients})

def forum(request):
    return render(request,'forum.html')


def forum_view(request):
    if request.method == "POST":
        if "submit_post" in request.POST:  # Handle Post Submission
            content = request.POST.get("post_content")
            ForumPost.objects.create(content=content)  # Post remains unapproved until admin approval

        elif "submit_response" in request.POST:  # Handle Response Submission
            post_id = request.POST.get("post_id")
            content = request.POST.get("response_content")
            post = ForumPost.objects.get(id=post_id)
            ForumResponse.objects.create(post=post, content=content)  # Response remains unapproved

        return redirect("forum")

    posts = ForumPost.objects.filter(is_approved=True).order_by("-created_at")
    return render(request, "forum.html", {"posts": posts})




# Create your views here.
