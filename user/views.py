from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.


def registers(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = User(username = username,password = password)
        user.save()
        login(request,user)
        return redirect("index")

    else:

        return render(request,"register.html",{"form":form})

def logins(request):

    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        if user is None:
            messages.success(request,"WeDontFindThisUser.PleaseTryAgain")
            return redirect("/user/login")

        else:
            login(request,user)
            messages.success(request,"Cong.Welcome Our Page")
            return redirect("index")
            



    return render(request,"login.html",{"form":form})

def logouts(request):

    logout(request)
    messages.success(request,"WeWillWaitAgain")

    return redirect("index")