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
from .views import inicio, ingresar, registrar, cerrar
from Clientes.views import clientes
from Libros.views import libros

urlpatterns = [
    path('', inicio, name='inicio'),
    path('libros/', libros, name='libros'),
    path('clientes/', clientes, name='clientes'),
    path('ingresar/', ingresar, name='ingresar'),
    path('registrar/', registrar, name='registrar'),
    path('cerrar/', cerrar, name='cerrar'),
    path('admin/', admin.site.urls),
]
