from django.shortcuts import render
from django.urls import path
from . import views
# Create your views here.
urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
]