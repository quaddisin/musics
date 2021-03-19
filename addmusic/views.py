from django.shortcuts import render,redirect,get_object_or_404
from django.http import request
from .forms import Addmusicform
from .models import AddMusic
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='http://127.0.0.1:8000/user/login/')
def addmusic(request):
    
    form = Addmusicform(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("addmusic")
        
    else:
        return render(request,"addmusic.html",{"form":form})
@login_required(login_url='http://127.0.0.1:8000/user/login/')
def musicdetail(request,name):

    result = AddMusic.objects.filter(musicname= name).first()

    return render(request,"musicdetails.html",{"result":result})

@login_required(login_url='http://127.0.0.1:8000/user/login/')
def deletemusic(request,name):
    music = AddMusic.objects.filter(musicname = name).first()
    music.delete()
    return redirect("index")

@login_required(login_url='http://127.0.0.1:8000/user/login/')
def updatemusic(request,name):
    musicform = AddMusic.objects.get(musicname = name)
    form = Addmusicform(request.POST or None , request.FILES or None,instance = musicform)
    if form.is_valid():
        form.save()
        messages.success(request,"Başarıyla Güncellendi")
        return redirect("index")

    else:

        return render(request,"updatemusic.html",{"form":form})