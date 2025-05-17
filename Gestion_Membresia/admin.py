from django.contrib import admin

from .models import membresia

@admin.register(membresia)
class MembresiaAdmin(admin.ModelAdmin):
    list_display = ('Tipo_Membresia', 'Precio')  # columnas que quieres mostrar en el listado
    search_fields = ('Tipo_Membresia',) 