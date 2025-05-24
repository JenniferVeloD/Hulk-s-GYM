from django.contrib import admin
from .models import Miembro

# Register your models here.
@admin.register(Miembro)
class MiembroAdmin(admin.ModelAdmin):
    """
    La clase personaliza como se muestra el modelo 'Miembro'
    """
    exclude = ('Fecha_final',)
    """
    Campo 'Fecha_final' que es excluido del formulario de edición y creación en el panel de administración
    """
    list_display = ('Nombre', 'Apellidos', 'Telefono', 'Membrecia', 'Fecha_inicio', 'Fecha_final')
    """
    Campos que se muestran como columnas en la página de lista de miembros en el panel de administrador de Django
    """
    search_fields = ('Nombre', 'Apellidos', 'Telefono')
    """
    Campos por los cuales se puede realizar una búsqueda en la lista de miembros
    """
    list_filter = ('Membrecia',)
    """
    Filtrar miembros por el tipo de membresía
    """