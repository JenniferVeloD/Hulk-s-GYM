from django.contrib import admin
from .models import membresia

@admin.register(membresia)
class MembresiaAdmin(admin.ModelAdmin):
    list_display = ('Tipo_Membresia', 'Precio', 'Duracion_dias')
    search_fields = ('Tipo_Membresia',) 