from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')
        User.objects.create(username=uname, email=email, password=pwd)
        messages.success(request, 'Registration successful.')
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'login.html')
    return render(request, 'login.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')
# Create your views here.
def abc(request):
    return render(request,'abc.html')
def mca101(request):
    return render(request,'mca101.html')    
def mca102(request):
    return render(request,'mca102.html')
def mca103(request):
    return render(request,'mca103.html')
def mca104(request):
    return render(request,'mca104.html')
def mca105(request):
    return render(request,'mca105.html')
def mca106(request):
    return render(request,'mca106.html')
def mca107(request):
    return render(request,'mca107.html')
def mca108(request):
    return render(request,'mca108.html')
def mca201(request):
    return render(request,'mca201.html') 
def mca202(request):
    return render(request,'mca202.html')  
def mca203(request):
    return render(request,'mca203.html')
def mca204(request):
    return render(request,'mca204.html')  
def mca205(request):
    return render(request,'mca205.html') 
def mca206(request):
    return render(request,'mca206.html') 
def mca207(request):
    return render(request,'mca207.html')    
def mca208(request):
    return render(request,'mca208.html')
def mca209(request):
    return render(request,'mca209.html')
def mca301(request):
    return render(request,'mca301.html')
def mca302(request):
    return render(request,'mca302.html')
def mca303(request):
    return render(request,'mca303.html') 
def mca304(request):
    return render(request,'mca304.html')
def mca305(request):
    return render(request,'mca305.html')
def mca306(request):
    return render(request,'mca306.html')  
def mca307(request):
    return render(request,'mca307.html')         
def mca308(request):
    return render(request,'mca308.html')  
def mca309(request):
    return render(request,'mca309.html')
def mca310(request):
    return render(request,'mca310.html')
def mca401(request):
    return render(request,'mca401.html')  
def mca402(request):
    return render(request,'mca402.html')