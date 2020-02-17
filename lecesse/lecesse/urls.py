"""lecesse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    #direcciones del modulo base
    path('', include('base.urls')),
    #direcciones del modulo users
    path('users/', include('users.urls')),
    #direcciones del modulo phase one
    path('phase_one/', include('phase_one.urls')),
    #redirige al index luego de hacer el login
    path('', RedirectView.as_view(url="/home/index/")),
    # muestra el login de inicio
	path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login'),
	#Logout
	path('logout/', auth_views.LogoutView.as_view(template_name='registration/login.html'),
        name='logout'),
]
