from django.shortcuts import render
from .models import Cliente

ENCABEZADO = "Clientes"

def clientes(request):
    context = {
        "encabezado": ENCABEZADO,
        "clientes": Cliente.objects.all(),
        "field_keys": [field.attname for field in Cliente._meta.get_fields()]
    }

    return render(request=request, template_name='clientes.html', context=context)
