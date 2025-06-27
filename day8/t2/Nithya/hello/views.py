from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello,Django")

def pen(request):
    a='<h1>Welcome to training class</h1>'
    return HttpResponse(a)
