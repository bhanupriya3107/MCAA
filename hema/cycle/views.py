from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def demo(request):
    temp=loader.get_template('index.html')
    return HttpResponse(temp.render())
def bhanu(request):
    a='<marquee><h3>My self Bhanu,i am from MCA</h3></marquee>' 
    return HttpResponse(a)   