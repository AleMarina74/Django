from django.db import models

class Libro(models.Model):
    titulo= models.CharField(max_length=200, verbose_name='Nombre')
    autor= models.ForeignKey(
        'autor.Autor', 
        on_delete=models.DO_NOTHING,
        verbose_name='Autor'
    )
    genero= models.ForeignKey(
        'genero.Genero',
        on_delete=models.DO_NOTHING,
        verbose_name='Genero'
    )
    isbn= models.BigIntegerField()

    borrado= models.BooleanField(default=False, verbose_name='Borrado')

    disponible= models.BooleanField(default=True, verbose_name='Disponible')

    #portada = models.ImageField(upload_to='imagenes/', null =True, verbose_name='Portada')

    def __str__(self):
        return self.titulo
    
    @property
    def nombre_autor(self):
        return self.autor.nombre
    
    @property
    def nombre_genero(self):
        return self.genero.nombre
    
    def borrado_logico(self):
        if self.borrado == False:
            self.borrado = True
            self.disponible = False
            super().save()

    def restarurar(self):
        if self.borrado:
            self.borrado = False
            self.disponible = True
            super().save()

    def prestado(self):
        self.disponible = False
        super().save()
    
    def devuelto(self):
        self.disponible = True
        super().save()

    def delete(self,*args,**kwargs):
        self.borrado_logico()