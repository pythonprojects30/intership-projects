from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        cpassword = request.POST['password2']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username,email=email)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "password not match")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
