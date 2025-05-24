from django.contrib import admin
from .models import Categoria, Proveedor, Producto

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """
    La clase configura como se muestra el modelo 'Categoria'
    """
    list_display = ('nombre', 'descripcion')
    """
    Campos que se muestran como columnas en la página de lista de categorías en 
    el panel de administrador
    """
    search_fields = ('nombre',)
    """
    Campo por los que se puede realizar una búsqueda en la lista de categorías
    """

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    """
    La clase configura como se muestra el modelo 'Proveedor'
    """
    list_display = ('nombre', 'correo', 'telefono')
    """
    Campos que se muestran como columnas en la página de lista de proveedores en 
    el panel de administrador
    """
    search_fields = ('nombre', 'correo')
    """
    Campos por los que se puede realizar una búsqueda en la lista de proveedores
    """

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """
    La clase configura como se muestra el modelo 'Producto'
    """
    list_display = ('id', 'nombre', 'precio', 'categoria', 'proveedor', 'stock', 'fecha_actualizacion')
    """
    Campos que se muestran como columnas en la página de lista de productos en 
    el panel de administrador
    """
    list_filter = ('categoria', 'proveedor')
    """
    Campos por los cuales se puede filtrar la lista de productos en el panel de administración
    """
    
    search_fields = ('nombre', 'id')
    """
    Campos por los que se puede realizar una búsqueda en la lista de productos
    """
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    """
    Campos de solo lectura en el formulario de modificación del producto.
    """