from django.forms import ModelForm
from .models import Libro

class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo',]