"""proect5o URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import base.views as views
urlpatterns = [
    path('quantum_computer/', views.quantum_computer,name='quantum_computer'),
    path('breaking_rsa/', views.breaking_rsa,name='breaking_rsa'),
    path('rsa/', views.rsa,name='rsa'),
    path('start/', views.start,name='start'),
    path('test/', views.test,name='test'),
    path('shor/', views.shor,name='shor'),
    path('shor_back/', views.shor_back,name='shor_back'),
    path('doc/', views.doc,name='doc'),
    path('testing/', views.testing,name='testing'),
    path('start_eve/', views.start_eve,name='start_eve'),

]
