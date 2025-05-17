from django.contrib import admin
from .models import Equipo

# Register your models here.
@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('id','Nombre_Equipo', 'categoria', 'cantidad', 'marca')
    search_fields = ('id','nombre', 'categoria', 'marca')
    #list_filter = ('categoria', 'marca')
    list_editable= ('cantidad',)
