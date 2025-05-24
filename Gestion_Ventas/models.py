from django.db import models
from django.utils import timezone
from Gestion_Productos.models import Producto 


# Create your models here.

class Venta(models.Model):
    """
    Modelo cuya función es crear una venta en el sistema
    """
    fecha_venta = models.DateTimeField(default=timezone.now)
    """
    Campo para registrar automáticamente la fecha y hora de la venta
    """

    @property
    def total(self):
        return sum(detalle.subtotal for detalle in self.detalles.all())
    """
    Propiedad definido como atributo que calcula el total de la venta sumando los 
    subtotales de los objetos 'DetalleVenta' 
    """

    def __str__(self):
        return f"Venta #{self.id} - {self.fecha_venta.date()}"
    """
    Define como se muestra una instancia de 'Venta'
    """

class DetalleVenta(models.Model):
    """
    Modelo utilizado para crear el detalle de venta de un venta
    """
    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.CASCADE)
    """
    Clave foránea que establece una relación de uno a muchos con el modelo "Venta"
    """
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    """
    Clave foránea que establece una relación de uno a muchos con el modelo "Producto"
    """
    cantidad = models.PositiveIntegerField()
    """
    Campo que almacena la cantidad del producto vendido
    """

    @property
    def precio_unitario(self):
        return self.producto.precio 
    """
    Propiedad que obtiene el precio unitario del producto solicitado
    """

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario
    """
    Propiedad que calcula el subtotal de este detalle de venta.
    """

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
    """
    Define como se muestra una instancia de "DetalleVenta"
    """
