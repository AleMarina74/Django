from django.contrib import admin
from .models import Libro

@admin.register(Libro)

class LibroAdmin(admin.ModelAdmin):
    list_display=(
        'titulo',
    )

    list_filter=(
        'titulo',
        'genero',
        'autor',
        'borrado',
        'disponible',
    )

    ordering=(
        'titulo',
        'autor',
    )

    search_fields=(
        'titulo',
    
    )

