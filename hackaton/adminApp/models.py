from unicodedata import name
from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField( max_length=50)
    imagen = models.ImageField(upload_to="admin", blank=True, null=True)
    descripcion = models.CharField( max_length=300)
    precio = models.FloatField()    
    unidades = models.IntegerField()
    
    def __str__(self):
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    
        
