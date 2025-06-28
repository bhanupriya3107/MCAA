
from django.urls import path
from.import views

urlpatterns=[
    path('college/',views.college,name='college'),
    path('demo/',views.demo,name='demo'),

]
