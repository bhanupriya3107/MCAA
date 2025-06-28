from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def demo(request):
    a='<marquee><h3>Going TO Temple</h3></marquee>'
    return HttpResponse(a)
def bhanu(request):
    a='<marquee><h3>My self Bhanu,i am from MCA</h3></marquee>' 
    return HttpResponse(a)   