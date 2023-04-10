from django.db import models

# Create your models here.

class Cliente(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=50)
    celular = models.CharField(max_length=10)
    domicilio = models.CharField(max_length=100)
    estado = models.CharField(max_length=1)
    ISBN = models.CharField(max_length=18)

    def imprimirCliente(self):  
        return self.nombre, self.celular, self.domicilio, self.estado
    
    def __str__(self) -> str:
        return super().__str__()