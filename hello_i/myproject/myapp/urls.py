from django.shortcuts import render
from django.urls import path
from . import views
urlpatterns = [
   path('insert_employee/',views.insert_employee,name='insert_employee'),
]
# Create your views here.
