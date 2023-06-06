from django.db import models

class Usuario (models.Model):
    usuario= models.TextField(max_length=100)
    contrasenia=models.TextField(max_length=100)
    
    def __str__(self):
        return self.usuario