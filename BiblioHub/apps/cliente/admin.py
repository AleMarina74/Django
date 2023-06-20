from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)

class ClienteAdmin(admin.ModelAdmin):
    list_display=(
        'nombre',
        'apellido',
        'nombre',
    )
    
    
    list_filter=(
        'active',
        'disponible',
    )
    
    ordering=(
        'nombre',
        'apellido',
        'dni',
    )

    search_fields=(
        'nombre',
        'apellido',
        'dni',
    )


