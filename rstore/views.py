from django.shortcuts import render
from .models import serv


def index(request):
    service = serv.objects.all()
    return render(request, 'index.html', {'service': service})

def test(request):
    serv1 = serv.objects.all()
    return render(request, 'test.html', {'test' : serv1})


def registerlogin(request):
    
    return render(request, 'register-login.html')

def services(request):
    service = serv.objects.all()
    return render(request, 'services.html', {'service' : service})

def logout(request):
    return render(request, 'logout.html')

def scart(request):
    return render(request, 'scart.html')

def login(request):
    if method == 'post':
        pass
    else:
        return render(request, 'register-login.html')

def register(request):
    if method == 'post':
        pass
    else:
        return render(request, 'register-login.html')

