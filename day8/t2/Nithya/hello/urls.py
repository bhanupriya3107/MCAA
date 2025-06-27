from django.urls import path

# Create your views here.
from.import views
urlpatterns=[
    path('home/',views.home,name='home'),
    path('pen/',views.pen,name='pen'),
         ]
