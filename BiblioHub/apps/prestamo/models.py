from django.db import models
from ..cliente.models import Cliente
from ..libro.models import Libro

class Prestamo(models.Model):
    libro = models.ForeignKey(
        'libro.Libro', 
        on_delete=models.DO_NOTHING,
        related_name='libros'
    )
    cliente = models.ForeignKey(
        'cliente.Cliente',
        on_delete=models.DO_NOTHING,
        related_name='clientes'
    )
    fecha_prestamo = models.DateField(null=True, blank=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    devolucion = models.BooleanField(default=False)

    def _str_(self):
        return f"{self.libro.titulo} - {self.cliente.nombre} {self.cliente.apellido}"
    
    def prestar(self):
        Libro.prestado()
        Cliente.prestado()
    
    def devoluciones(self):
        self.devolucion = True
        self.fecha_devolucion = self.fecha_devolucion
        super().save()
        Libro.devuelto()
        Cliente.devuelto()