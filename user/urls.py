from django.contrib import admin
from django.urls import path
from .views import registers,logins,logouts
app_name = "users"
urlpatterns = [
    path("register/",registers,name="registers"),
    path("login/",logins,name="login"),
    path("logout/",logouts,name="logout")

]