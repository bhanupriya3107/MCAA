from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def college(request):
    return HttpResponse("Welcome to college!")

def demo(request):
    a='<marquee><h1>Welcome to training class</h1></marquee>'
    return HttpResponse(a)    

