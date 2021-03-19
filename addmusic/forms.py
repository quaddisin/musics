from django import forms
from django.db import models
from .models import AddMusic
class Addmusicform(forms.ModelForm):
    class Meta:
        model = AddMusic
        fields = ["musicname","musicactor","musicyear","musiccontent","musicfile"]
    