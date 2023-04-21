from django.shortcuts import render
from .models import Libro
from django.contrib.auth.decorators import login_required

@login_required(login_url='ingresar')
def libros(request):
    context = {
        "encabezado": "Libros",
        "libros": Libro.objects.all(),
        "field_keys": [field.attname for field in Libro._meta.get_fields()],
        "USER": request.user
    }
    return render(request=request, template_name='libros.html', context=context)
