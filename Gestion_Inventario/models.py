from django.db import models

from django.utils.html import format_html
# Create your models here.


class Equipo(models.Model):
    """
     Modelo que representa un equipo en el gimnasio
    """
    nombre = models.CharField(max_length=100)
    """
    Campo que representa el nombre del equipo
    """
    categoria = models.CharField(max_length=50)
    """
    Campo que representa la categoria del equipo
    """
    cantidad = models.PositiveIntegerField()
    """
    Campo que representa la cantidad del tipo de equipo en el inventario
    """
    marca = models.CharField(max_length=100)
    """
    Campo que representa la marca del equipo
    """

    def __str__(self):
        return f"{self.nombre} ({self.marca})"
    """
    Define cómo se muestra una instancia de 'Equipo'
    """
    
    def Nombre_Equipo(self):
        if self.cantidad<= 0:
            return format_html('<span style="color: red;">{0}</span>'.format(self.nombre))
        return f"{self.nombre} "
    """
    Devuelve el nombre del equipo, destacandolo en rojo si la cantidad es cero o menos
    """