from django.contrib import admin
from .models import Miembro

# Register your models here.
@admin.register(Miembro)
class MiembroAdmin(admin.ModelAdmin):
    exclude = ('Fecha_final',)
    list_display = ('Nombre', 'Apellidos', 'Telefono', 'Membrecia', 'Fecha_inicio', 'Fecha_final')
    search_fields = ('Nombre', 'Apellidos', 'Telefono')
    list_filter = ('Membrecia',)