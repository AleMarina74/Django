from django.contrib import admin
from .models import Genero

@admin.register(Genero)

class GeneroAdmin(admin.ModelAdmin):
    list_display=('nombre',)
# Register your models here.
