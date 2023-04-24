from django.db import models

# Create your models here.
class Libro(models.Model):
    USBN = models.CharField(max_length=18, null=True)
    titulo = models.CharField(max_length=200,null=True)
    autor = models.CharField(max_length=100,null=True)
    estado = models.CharField(max_length=1, default='D')
    dni = models.CharField(max_length=8, default = '', blank =True)
