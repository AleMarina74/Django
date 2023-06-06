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
from apps.cliente.views import clients, client,ClientesTemplateView,ClienteCreate,ClienteUpdate,ClienteDetail
from apps.libro.views import BooksTemplateView, book, BookTemplateView, BookCreate, BookDelete,BookDetail,BookList,BookUpdate

urlpatterns = [
    path('', home, name='home'),
    path('libros/', BooksTemplateView.as_view(), name='books'),
    path('libro/<int:id>', BookTemplateView.as_view(), name='book'),
    path('libros/list/',BookList.as_view(), name='listbook'),
    path('libros/create/', BookCreate.as_view(), name='createbook'),
    path('libros/<int:pk>/detail/',BookDetail.as_view(), name='detailbook'),
    path('libros/<int:pk>/update/', BookUpdate.as_view(), name='updatebook'),
    path('libros/<int:pk>/delete/', BookDelete.as_view(), name='deletebook'),
    path('clientes/', ClientesTemplateView.as_view(), name='clients'),
    #path('cliente/<int:id>', client, name='client'),
    path('cliente/create/', ClienteCreate.as_view(), name='createclient'),
    path('cliente/<int:id>/', ClienteDetail.as_view(), name='detailclient'),
    path('cliente/<int:pk>/update/', ClienteUpdate.as_view(), name='updateclient'),
    path('perfil/', profile, name='profile'),
    path('ingresar/', user_login, name='login'),
    path('registrar/', user_signup, name='signup'),
    path('cerrar/', user_logout, name='logout'),
    path('admin/', admin.site.urls),
]
