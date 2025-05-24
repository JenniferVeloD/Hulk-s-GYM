from django.db import models
from Gestion_Membresia.models import membresia 
from datetime import timedelta, date

# Create your models here.
class Miembro(models.Model):
    """
    Modelo que permite gestionar un miembro del gimnasio
    """
    Nombre = models.CharField(max_length=100)
    """
    Campo que representa el nombre del miembro
    """
    Apellidos = models.CharField(max_length=100)
    """
    Campo que representa el apellido del miembro
    """
    Membrecia = models.ForeignKey(membresia, on_delete=models.CASCADE)
    """
    Clave foránea que enlaza que realciona al miembro con su tipo de membresía
    """
    Telefono = models.CharField(max_length=15)
    """
    Campo que representa el teléfono del miembro
    """
    Fecha_inicio = models.DateField(auto_now_add=True)
    """
    Campo que representa la fecha de inicio de la membresía miembro
    """
    Fecha_final = models.DateField(blank=True, null=True)
    """
    Campo que representa la fecha de fin de la membresía miembro
    """

    def save(self, *args, **kwargs):
        if not self.Fecha_final and self.Membrecia:
            self.Fecha_final = date.today() + timedelta(days=self.Membrecia.Duracion_dias)
        super().save(*args, **kwargs)
    """
    Calcula automaticamente "Fecha_final"
    """

    def fecha_inicio_formateada(self):
        return self.Fecha_inicio.strftime('%d de %B del %Y')
    """
    Formatea la 'Fecha_inicio' del miembro a un formato legible en español
    """

    def fecha_final_formateada(self):
        return self.Fecha_final.strftime('%d de %B del %Y') if self.Fecha_final else "Sin fecha final"
    """
    Formatea la 'Fecha_final' del miembro a un formato legible en español
    """

    def __str__(self):
        return f"{self.Nombre} {self.Apellidos}"
    """
    Define cómo se muestra una instancia de 'Miembro'
    """
