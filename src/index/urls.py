
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("",showIndex, name="showIndex"),
    path("showtest/",showtest,name="showtest"),
]
