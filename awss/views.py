from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.views.generic import TemplateView
# Create your views here.


def home(request):
    return render(request, 'awss/Home.html')


def service(request):
    return render(request, 'awss/Services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        description = request.POST['message']
        user_contact = Contact.objects.create(name=name, email=email, description=description)
        user_contact.save()
        return redirect('awss:awss-home')
    return render(request, 'awss/Contact.html')


def about(request):
    return render(request, 'awss/About.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect('awss:awss-signout')
    else:
        if request.method == 'POST':
            user_name = request.POST['name']
            password = request.POST['Password']
            user = authenticate(request, username=user_name, password=password)
            if user is not None:
                login(request, user)
                return redirect('awss:awss-signout')
    return render(request, 'awss/Login.html')


def signout(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            logout(request)
            return redirect('awss:awss-login')
        return render(request, 'awss/Signout.html')
    return redirect('awss:awss-login')


def signup(request):
    if request.user.is_authenticated:
        return redirect('awss:awss-signout')
    if request.method == 'POST':
        user_name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 == pass2:
            print(f'{user_name, email, pass1, pass2}')
            try:
                user_email = User.objects.get(email=email)
                print(f'{user_email.email} already exist')
            except User.DoesNotExist:
                try:
                    name_user = User.objects.get(username=user_name)
                    print(f'{name_user.username} already exist')
                except User.DoesNotExist:
                    user = User.objects.create_user(email=email, username=user_name, password=pass1)
                    user.save()
                    return redirect('awss:awss-login')
    return render(request, 'awss/Signup.html')


def scan(request):
    return render(request, 'awss/Scan.html')
