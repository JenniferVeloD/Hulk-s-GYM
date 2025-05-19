from django.db import models
from django.utils import timezone
from Gestion_Productos.models import Producto 


# Create your models here.

class Venta(models.Model):
    fecha_venta = models.DateTimeField(default=timezone.now)

    @property
    def total(self):
        return sum(detalle.subtotal for detalle in self.detalles.all())

    def __str__(self):
        return f"Venta #{self.id} - {self.fecha_venta.date()}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()

    @property
    def precio_unitario(self):
        return self.producto.precio 

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

