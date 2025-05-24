from django.contrib import admin
from .models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    """
    La clase configura como se muestra el modelo 'Empleado'
    """
    list_display = ('usuario', 'direccion', 'puesto', 'fecha_contratacion')
    """
    Campos que se muestran como columnas en la página de lista de empleados en 
    el panel de administrador
    """
    search_fields = ('usuario__username', 'usuario__email', 'usuario__first_name', 'usuario__last_name')
    """
    Campos por los que se puede realizar una búsqueda en la lista de empleados 
    """
    list_filter = ('puesto',)
    """
    Campos por los cuales se puede filtrar la lista de empleados en el panel de administración
    """