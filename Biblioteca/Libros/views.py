from django.shortcuts import render
from .models import Libro
from django.contrib.auth.decorators import login_required

@login_required(login_url='ingresar')
def books(request):
    context = {
        "page_heading": "Libros",
        "books": Libro.objects.all(),
        "field_keys": [field.attname for field in Libro._meta.get_fields()],
        "USER": request.user
    }
    return render(request=request, template_name='books.html', context=context)


@login_required(login_url='ingresar')
def book(request, id):
    books = Libro.objects.filter(id=id)
    context = {
        "page_heading": "Libro",
        "book": books[0] if len(books) else None,
        "USER": request.user
    }

    return render(request=request, template_name='book.html', context=context)