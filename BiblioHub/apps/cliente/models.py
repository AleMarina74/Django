from django.db import models
from apps.utils.models import Persona

class Cliente(Persona):

   # def imprimirCliente(self):  
    #    return self.nombre, self.celular, self.domicilio, self.estado
    
    @classmethod
    def keys(self):
        return [field.attname for field in self._meta.get_fields()]
    
    def __str__(self) -> str:
        return super().__str__()
