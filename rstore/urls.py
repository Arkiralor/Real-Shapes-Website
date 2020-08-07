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
    path('scart', views.scart, name = 'scart')
]