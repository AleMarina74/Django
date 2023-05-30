from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Cliente
from django.contrib.auth.decorators import login_required

@login_required(login_url='ingresar')
def clients(request):
    paginator = Paginator(Cliente.objects.all(), 10)
    page_number = request.GET.get("page")
    context = {
        "page_heading": "Clientes",
        "clients": paginator.get_page(page_number),
        "field_keys": [field.attname for field in Cliente._meta.get_fields()],
        "USER": request.user
    }

    return render(request=request, template_name='clients.html', context=context)

@login_required(login_url='ingresar')
def client(request, id):
    clients = Cliente.objects.filter(id=id)
    context = {
        "page_heading": "Cliente",
        "client": clients[0] if len(clients) else None,
        "USER": request.user
    }

    return render(request=request, template_name='client.html', context=context)

# Create your views here.
