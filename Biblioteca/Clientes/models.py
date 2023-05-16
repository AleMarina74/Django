from django.db import models

# Create your models here.

class Cliente(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=50)
    celular = models.CharField(max_length=10)
    domicilio = models.CharField(max_length=100)
    estado = models.CharField(max_length=1, default='D')
    ISBN = models.CharField(max_length=18, null=True, blank=True)

    def imprimirCliente(self):  
        return self.nombre, self.celular, self.domicilio, self.estado
    
    @classmethod
    def keys(self):
        return [field.attname for field in self._meta.get_fields()]
    
    def __str__(self) -> str:
        return super().__str__()