from django.db import models
from django.contrib.auth.models import User

class Empleado(models.Model):
    RECEPCIONISTA = 'recepcionista'
    ADMIN = 'admin'
    PUESTO_CHOICES = [
        (RECEPCIONISTA, 'Recepcionista'),
        (ADMIN, 'Administrador'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    puesto = models.CharField(max_length=20, choices=PUESTO_CHOICES, default=RECEPCIONISTA)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f"{self.usuario.get_full_name()} - {self.puesto}"
