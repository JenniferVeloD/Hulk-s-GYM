from django.db import models
from django.contrib.auth.models import User

class Empleado(models.Model):
    """
    Modelo para registrar un empleado 
    """
    RECEPCIONISTA = 'recepcionista'
    """
    Constante para el valor del puesto de recepcionista
    """
    ADMIN = 'admin'
    """
    Constante para el valor del puesto de administrador
    """
    PUESTO_CHOICES = [
        (RECEPCIONISTA, 'Recepcionista'),
        (ADMIN, 'Administrador'),
        """
        define las opciones disponibles para el campo 'puesto'
        """
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    """
    Clave foránea uno a uno que relaciona a cada empleado con un usuario
    """
    direccion = models.CharField(max_length=100)
    """
    Campo para guardar la dirección del empleado
    """
    puesto = models.CharField(max_length=20, choices=PUESTO_CHOICES, default=RECEPCIONISTA)
    """
    Define el puesto de trabajo del empleado utilizando 'PUESTO_CHOICES
    """
    fecha_contratacion = models.DateField()
    """
    Campo para registrar la fecha en que el empleado fue contratado
    """

    def __str__(self):
        """
        Define cómo se muestra una instancia de 'Empleado'
        """
        return f"{self.usuario.get_full_name()} - {self.puesto}"
