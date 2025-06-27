from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def monday(request):
    return HttpResponse("I was born on Monday")

def pen(request):
    a='<marquee><h1> I am a good pen. Use me to get good marks</h1></marquee>'
    return HttpResponse(a)
