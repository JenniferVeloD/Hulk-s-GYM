from django.db import models

from django.utils.html import format_html
# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    cantidad = models.PositiveIntegerField()
    marca = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.marca})"
    
    def Nombre_Equipo(self):
        if self.cantidad<= 0:
            return format_html('<span style="color: red;">{0}</span>'.format(self.nombre))
        return f"{self.nombre} "
