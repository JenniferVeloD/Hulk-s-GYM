from django.db import models

# Create your models here.

class membresia(models.Model):
    Tipo_Membresia = models.CharField(max_length=150) 
    Precio= models.DecimalField(max_digits=10, decimal_places=2)
    Duracion_dias = models.PositiveIntegerField()

    def __str__(self): 
        return self.Tipo_Membresia
