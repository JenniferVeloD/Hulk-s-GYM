from django.contrib import admin
from .models import Equipo

# Register your models here.
@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    """
    La clase configura como se muestra el modelo 'Equipo'
    """
    list_display = ('id','Nombre_Equipo', 'categoria', 'cantidad', 'marca')
    """
    Campos que se muestran como columnas en la página de lista de inventario en 
    el panel de administrador
    """
    search_fields = ('id','nombre', 'categoria', 'marca')
    """
    Campos por los que se puede realizar una búsqueda en la lista de inventario
    """
    #list_filter = ('categoria', 'marca')
    list_editable= ('cantidad',)
    """
    Campo que se puede modificar directamente en la tabla en la lista los objetos
    """
