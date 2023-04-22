from django.shortcuts import render
from .models import Cliente
from django.contrib.auth.decorators import login_required

@login_required(login_url='ingresar')
def clients(request):
    context = {
        "page_heading": "Clientes",
        "clients": Cliente.objects.all(),
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
