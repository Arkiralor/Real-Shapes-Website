from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def registerlogin(request):
    return render(request, 'register-login.html')

def services(request):
    return render(request, 'services.html')

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
