from django.shortcuts import render
from .models import Cliente
from django.contrib.auth.decorators import login_required


ENCABEZADO = "Clientes"

@login_required(login_url='ingresar')
def clientes(request):
    context = {
        "encabezado": ENCABEZADO,
        "clientes": Cliente.objects.all(),
        "field_keys": [field.attname for field in Cliente._meta.get_fields()],
        "USER": request.user
    }

    return render(request=request, template_name='clientes.html', context=context)
