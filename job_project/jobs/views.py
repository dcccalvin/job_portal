from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.conf import settings
from django.core.mail.message import EmailMessage

def index(request):
    return render(request, "noot.html")

def about(request):
    return render(request, 'about.html')

def signin(request):
    if request.method == "POST":
        uname = request.POST.get("Username")
        password = request.POST.get("password")
        myuser = authenticate(username=uname, password=password)
        if myuser is not None:
            login(request, myuser)
            return redirect('/')
        else:
            return redirect('/signin/')
    return render(request, 'signin.html')

def signup(request):
    if request.method == "POST":
        uname = request.POST.get("Username")
        email = request.POST.get("Email")
        password = request.POST.get("password")
        # Add confirm password later

        try:
            if User.objects.get(username=uname):
                messages.info(request, "Sorry, the username is taken!")
                return redirect('/signup/')
        except User.DoesNotExist:
            pass

        try:
            if User.objects.get(email=email):
                messages.info(request, "Email is already taken!")
                return redirect('/signup/')
        except User.DoesNotExist:
            pass

        myuser = User(username=uname, email=email)
        myuser.set_password(password)  # Set the hashed password
        myuser.save()

        messages.success(request, "Created account successfully!")
        return redirect('/')

    return render(request, 'signup.html')