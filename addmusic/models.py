from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class AddMusic(models.Model):

    musicname = models.CharField(verbose_name="Music Name",max_length=30)
    musicactor = models.CharField(verbose_name="Music Actor",max_length=20)
    musicyear = models.CharField(verbose_name="Music Year",max_length=4)
    musiccontent = RichTextField(verbose_name="Music Content",max_length=600)
    musicfile = models.FileField(blank=True,null=True,verbose_name="Music Photo")
    def __str__(self):
        return self.musicname
    