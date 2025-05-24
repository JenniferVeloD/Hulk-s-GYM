from django.db import models

# Create your models here.

class Categoria(models.Model):
    """
    Modelo que registra una categoría para clasificar productos
    """
    nombre = models.CharField(max_length=100)
    """
    Campo que representa el nombre de la categoría
    """
    descripcion = models.TextField(blank=True, null=True)
    """
    Campo que representa la descripción de la categoría
    """
    
    def __str__(self):
        return self.nombre
    """
    Define cómo se muestra una instancia de 'Categoria'
    """
    
    class Meta:
        verbose_name_plural = "Categorias"
    """
    Legible para humanos para el modelo en el panel de administración
    """

class Proveedor(models.Model):
    """
    Modelo que registra un proveedor de productos
    """
    nombre = models.CharField(max_length=100)
    """
    Campo que representa el nombre del proveedor
    """
    correo = models.EmailField(blank=True, null=True)
    """
    Campo que representa el correo del proveedor
    """
    telefono = models.CharField(max_length=20, blank=True, null=True)
    """
    Campo que representa el telefono del proveedor
    """
    direccion = models.TextField(blank=True, null=True)
    """
    Campo que representa la doreccion del proveedor
    """
    
    def __str__(self):
        return self.nombre
    """
    Define cómo se muestra una instancia de 'Proveedor'
    """
    
    class Meta:
        verbose_name_plural = "Proveedores"
    """
    Legible para humanos para el modelo en el panel de administración
    """

class Producto(models.Model):
    """
    Modelo que registra un producto en el inventario
    """
    nombre = models.CharField(max_length=200)
    """
    Campo que representa el nombre de producto
    """
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    """
    Campo que representa el precio de producto
    """
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='productos')
    """
    Clave foránea que relaciona el producto a su categoría.
    """
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, related_name='productos')
    """
    Clave foránea que relaciona el producto con su proveedor.
    """
    stock = models.PositiveIntegerField(default=0)
    """
    Campo que representa el stock de producto
    """
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    """
    Campo automatico que representa la fecha de registro del producto
    """
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    """
    Campo automatico que representa la fecha de actualización del producto
    """
    
    def __str__(self):
        return f"{self.nombre} (ID: {self.id})"
    """
    Define cómo se muestra una instancia de 'Producto'
    """
