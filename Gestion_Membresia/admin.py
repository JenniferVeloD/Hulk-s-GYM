from django.contrib import admin
from .models import membresia

@admin.register(membresia)
class MembresiaAdmin(admin.ModelAdmin):
    """
    La clase configura como se muestra el modelo 'membresia'
    """
    list_display = ('Tipo_Membresia', 'Precio', 'Duracion_dias')
    """
    Campos que se muestran como columnas en la página de lista de membresías en 
    el panel de administrador
    """
    search_fields = ('Tipo_Membresia',) 
    """
    Campo por los que se puede realizar una búsqueda en la lista de categorías
    """