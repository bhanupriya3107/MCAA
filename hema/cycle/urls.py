from django.shortcuts import render
from django.urls import path
from.import views
# Create your views here.
urlpatterns=[
    path('demo/',views.demo,name='demo'),
    path('bhanu/',views.bhanu,name='bhanu'),
]