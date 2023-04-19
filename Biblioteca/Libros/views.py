from django.shortcuts import render
from .models import Libro

ENCABEZADO = "Libros"

def libros(request):
    context = {
        "encabezado":ENCABEZADO,
        "libros": Libro.objects.all(),
        "field_keys": [field.attname for field in Libro._meta.get_fields()]
    }
    return render(request=request, template_name='libros.html', context=context)
