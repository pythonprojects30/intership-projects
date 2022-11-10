from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse

from django.shortcuts import render, redirect




def index(request):

    return render(request,"index.html")

#
def register(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword= request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')


            else:
                user = User.objects.create_user(password=password, username=username)
                user.save()
                return redirect('login')


        else:
                messages.info(request,"Password not matching")
                return redirect('register')




    return  render(request,"register.html")


def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('form')
        else:
            messages.info(request,"invalid details")
            return redirect("login")

    return render(request,"login.html")
# #
def form(request):

    return render(request, "form.html")
#
def msg(request):
    return render(request,"message.html")
def new(request):
    return render(request, "newpage.html")


def logout(request):
    auth.logout(request)
    return redirect("/")
#
#
