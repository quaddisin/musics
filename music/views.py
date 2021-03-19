from django.shortcuts import render,redirect
from django.http import request
from addmusic.models import AddMusic
def index(request):
    musics = AddMusic.objects.all()
    return render(request,"index.html",{"musics":musics})

