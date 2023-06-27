from django.db import models

class Autor(models.Model):
    nombre= models.TextField(max_length=50)
    
    def __str__(self):
        return self.nombre

