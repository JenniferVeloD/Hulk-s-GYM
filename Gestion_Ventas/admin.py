from django.contrib import admin
from .models import Venta, DetalleVenta

# Register your models here.

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1

class VentaAdmin(admin.ModelAdmin):
    inlines = [DetalleVentaInline]
    readonly_fields = ('fecha_venta',)

    def total_venta(self, obj):
        return obj.total
    total_venta.short_description = 'Total'

    list_display = ('id', 'fecha_venta', 'total_venta')

admin.site.register(Venta, VentaAdmin)
