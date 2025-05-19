from django.db import models
from Gestion_Membresia.models import membresia 
from datetime import timedelta, date

# Create your models here.
class Miembro(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    Membrecia = models.ForeignKey(membresia, on_delete=models.CASCADE)
    Telefono = models.CharField(max_length=15)
    Fecha_inicio = models.DateField(auto_now_add=True)
    Fecha_final = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.Fecha_final and self.Membrecia:
            self.Fecha_final = date.today() + timedelta(days=self.Membrecia.Duracion_dias)
        super().save(*args, **kwargs)

    def fecha_inicio_formateada(self):
        return self.Fecha_inicio.strftime('%d de %B del %Y')

    def fecha_final_formateada(self):
        return self.Fecha_final.strftime('%d de %B del %Y') if self.Fecha_final else "Sin fecha final"


    def __str__(self):
        return f"{self.Nombre} {self.Apellidos}"
