"""Biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import home, user_login, user_signup, user_logout, profile
from Clientes.views import clients, client
from Libros.views import books, book

urlpatterns = [
    path('', home, name='home'),
    path('libros/', books, name='books'),
    path('libro/<int:id>', book, name='book'),
    path('clientes/', clients, name='clients'),
    path('cliente/<int:id>', client, name='client'),
    path('perfil/', profile, name='profile'),
    path('ingresar/', user_login, name='login'),
    path('registrar/', user_signup, name='signup'),
    path('cerrar/', user_logout, name='logout'),
    path('admin/', admin.site.urls),
]
