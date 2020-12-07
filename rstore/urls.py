from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('services', views.services, name = 'services'),
    path('registerlogin', views.registerlogin, name = 'registerlogin'),
    path('register', views.registerlogin, name = 'register'),
    path('login', views.registerlogin, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('scart', views.scart, name = 'scart'),
    path('contact', views.contact, name = 'contact'),
    path('about', views.about, name = 'about'),
    path('messages', views.messages, name = 'messages'),
    path('test', views.test, name = 'test'),
    path('clients', views.clients, name = 'clients')
    ##path('mantra', views.test, name = 'mantra')

]