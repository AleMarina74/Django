"""
URL configuration for BiblioHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from apps.cliente.views import clients, client,ClientesTemplateView,ClienteCreate,ClienteUpdate,ClienteDetail,ClienteDelete
from apps.libro.views import BooksTemplateView, book, BookTemplateView, BookCreate, BookDelete,BookDetail,BookList,BookUpdate
from apps.autor.views import  Autor, AutorCreate,AutorDetail,AutorList,AutorUpdate
from apps.genero.views import  Genero, GeneroCreate,GeneroDetail,GeneroList,GeneroUpdate
from apps.prestamo.views import PrestamoCreate, PrestamoDetail, PrestamoList, PrestamoUpdate, prestamosviews, prestamoviews, PrestamoCreateView, DevolucionCreateView

urlpatterns = [
    path('', home, name='home'),
    path('libros/', BooksTemplateView.as_view(), name='books'),
    path('libro/<int:id>', BookTemplateView.as_view(), name='book'),
    path('libros/list/',BookList.as_view(), name='listbook'),
    path('libros/create/', BookCreate.as_view(), name='createbook'),
    path('libros/<int:pk>/detail/',BookDetail.as_view(), name='detailbook'),
    path('libros/<int:pk>/update/', BookUpdate.as_view(), name='updatebook'),
    path('libros/<int:pk>/delete/', BookDelete.as_view(), name='deletebook'),
    path('clientes/',ClientesTemplateView.as_view(), name='clients'),
    path('clientes/<int:id>', client, name='client'),
    path('cliente/create/', ClienteCreate.as_view(), name='createclient'),
    #path('cliente/<int:id>/', ClienteDetail.as_view(), name='detailclient'),
    path('cliente/<int:pk>/update/', ClienteUpdate.as_view(), name='updateclient'),
    path('cliente/<int:pk>/delete/', ClienteDelete.as_view(), name='deleteclient'),
    path('autor/list/',AutorList.as_view(), name='listautor'),
    path('autor/create/', AutorCreate.as_view(), name='createautor'),
    path('autor/<int:pk>/detail/',AutorDetail.as_view(), name='detailautor'),
    path('autor/<int:pk>/update/', AutorUpdate.as_view(), name='updateautor'),
    path('genero/list/',GeneroList.as_view(), name='listgenero'),
    path('genero/create/', GeneroCreate.as_view(), name='creategenero'),
    path('genero/<int:pk>/detail/',GeneroDetail.as_view(), name='detailgenero'),
    path('genero/<int:pk>/update/', GeneroUpdate.as_view(), name='updategenero'),
    path('prestamos/', prestamosviews, name='prestamos'),
    path('prestamos/<int:id>', prestamoviews, name='prestamo'),
    path('prestamo/list/',PrestamoList.as_view(), name='listprestamo'),
    path('prestamo/create/', PrestamoCreateView.as_view(), name='createprestamo'),
    path('prestamo/<int:pk>/detail/', PrestamoDetail.as_view(), name='detailprestamo'),
    path('prestamo/<int:pk>/update/', DevolucionCreateView.as_view(), name='updateprestamo'),
    path('perfil/', profile, name='profile'),
    path('ingresar/', user_login, name='login'),
    path('registrar/', user_signup, name='signup'),
    path('cerrar/', user_logout, name='logout'),
    path('admin/', admin.site.urls),
]
