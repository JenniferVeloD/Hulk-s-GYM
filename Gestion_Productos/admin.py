from django.contrib import admin
from .models import Categoria, Proveedor, Producto

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono')
    search_fields = ('nombre', 'correo')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'categoria', 'proveedor', 'stock', 'fecha_actualizacion')
    list_filter = ('categoria', 'proveedor')
    search_fields = ('nombre', 'id')
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')