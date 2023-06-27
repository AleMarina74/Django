from django.db import models
from apps.utils.models import Persona

class Cliente(Persona):
    domicilio = models.CharField(max_length=200,null=True,blank=True)
    disponible = models.BooleanField(default=True, verbose_name='Disponibilidad')

   # def imprimirCliente(self):  
    #    return self.nombre, self.celular, self.domicilio, self.estado
    
    @classmethod
    def keys(self):
        return [field.attname for field in self._meta.get_fields()]
    
    def __str__(self) -> str:
        return super().__str__()
    
    
    def prestado(self):
        self.disponible = False
        super().save()

    def devuelto(self):
        self.disponible = True
        super().save()

    def borrado_logico(self):
        if self.active:
            self.active = False
            self.disponible = False
            super().save()

    def restarurar(self):
        if self.active == False:
            self.active = True
            self.disponible = True
            super().save()

    def delete(self,*args,**kwargs):
        self.borrado_logico()
   
