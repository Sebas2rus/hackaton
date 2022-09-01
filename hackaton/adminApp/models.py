from unicodedata import name
from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField( max_length=50)
    
    
    def __str__(self):
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        return self.nombre
        
        
class Productos(models.Model):
    nombre = models.CharField( max_length=50)
    imagen = models.ImageField(upload_to="admin", blank=True, null=True)
    descripcion = models.CharField( max_length=300)
    precio = models.FloatField()    
    unidades_disponibles = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=None)
                                  
    
    def __str__(self):
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        info = "%s $%s Unidades disponibles: %s" % (self.nombre,self.precio,self.unidades_disponibles)
        return info
    
        