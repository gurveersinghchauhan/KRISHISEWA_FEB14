from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from .forms import signupform
from .models import *

def index(request):
    return render(request , 'index.html')

def signin(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                login(request , user)
        else:
            return render(request , 'login.html')
    return redirect("/blogs")


def logoutuser(request):
    logout(request)
    return redirect("/")


def signup(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            form = signupform(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/signin')
        else:
            form = signupform()
        return render(request , 'signup.html', {'form':form})
    else:
        return redirect("/")


def blogs(request):
    blogs = blog.objects.all().order_by('-creation_date')  # Query all blogs and order by creation_date
    return render(request, 'blog_list.html', {'blogs': blogs})

def create_blog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        new_blog = blog(author=request.user ,title=title, content=content)
        new_blog.save()

    return redirect("/blogs")