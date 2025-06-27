from django.urls import path
from . import views

urlpatterns=[
    path('day1/',views.monday, name='day1'),
     path('pen/',views.pen, name='pen'),
    ]
