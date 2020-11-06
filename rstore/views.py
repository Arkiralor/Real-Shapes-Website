##from django.conf import settings
##from django.contrib.auth.models import user, auth
from django.shortcuts import render, redirect
from .models import serv, msg
from django.contrib.auth.decorators import login_required



def test(request):
    serv1 = serv.objects.all()
    return render(request, 'test.html', {'test' : serv1})

def index(request):
    service = serv.objects.filter(servishigh = True)[:8]
    return render(request, 'index.html', {'service': service})

def services(request):
    service = serv.objects.all()
    return render(request, 'services.html', {'service' : service})




def contact(request):
    if request.method == 'POST':
        mname = request.POST['visname']
        memail = request.POST['visemail']
        mphone = request.POST['visphone']
        mmsg = request.POST['vismsg']

        msg1 = msg(mname=mname, memail=memail, mphone=mphone, mmsg=mmsg)
        msg1.save()
        return redirect('contact')
    else:
        return render(request, 'contact.html')

##Messages
@login_required(login_url='/admin') #redirect when user is not logged in
def messages(request):
    message1 = msg.objects.all()
    return render(request, 'messages.html', {'message': message1})

def about(request):
    return render(request, 'aboutus.html')

##Unused definitions.

def registerlogin(request):
    
    return render(request, 'register-login.html')

def logout(request):
    return render(request, 'logout.html')

def scart(request):
    return render(request, 'scart.html')

def login(request):
    if request.method == 'post':
        pass
    else:
        return render(request, 'register-login.html')

def register(request):
    if request.method == 'post':
        pass
    else:
        return render(request, 'register-login.html')



