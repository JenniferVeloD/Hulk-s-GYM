from django.contrib import admin
from .models import Venta, DetalleVenta

# Register your models here.


class DetalleVentaInline(admin.TabularInline):
    """
    Clase que permite agregar "DetalleVenta" en un formulario de administracion "venta"
    """
    model = DetalleVenta
    """
    Modelo "DetalleVenta" de Django que se administra inline
    """
    extra = 1 
    """
     un formulario vacío después 
    """

    
class VentaAdmin(admin.ModelAdmin):

    """
    En esta clase se definen los datos y estructura de los objetos "venta"
    """
    inlines = [DetalleVentaInline]
    """"
    La clase DetalleVentaInline se incluye en el formulario de administración de Venta
    """
    readonly_fields = ('fecha_venta',)
    """
    El campo autogenerado 'fecha_venta' se incluye en el formulario de administración
    """

    def total_venta(self, obj):
        
        return obj.total
    
    """
    Metodo para calcular el total de la venta
    """
    total_venta.short_description = 'Total'
    """
    Muestra la cabecera de la columna para el resultado del método 'total_venta'

    """
    list_display = ('id', 'fecha_venta', 'total_venta')
    """
    id de la venta, fecha de la venta, y total de la venta son columnas que se muestran en la página
    de lista de cambios de los objetos "venta" en el panel de administrador de Django
    """

admin.site.register(Venta, VentaAdmin)
"""
Muestra el modelo "Venta" en el panel de administración de Django
"""