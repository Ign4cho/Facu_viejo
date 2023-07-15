from django.contrib import admin
from .models import Empleado, Categoria, Cliente, Proveedor, Producto, Factura, Provee, Venta

# Register your models here.

class AdminEmpleado(admin.ModelAdmin):
    list_display = ('dni', 'nombre')
    list_filter = ('codigo',)

class AdminProducto(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'precio')
    list_filter = ('nombre', 'precio')

class AdminCategoria(admin.ModelAdmin):
    list_diplay = ('codigo', 'nombre',)
    list_filter = ('codigo', 'nombre',)

class AdminCliente(admin.ModelAdmin):
    list_display = ('dni', 'nombre')
    list_filter = ('dni', 'nombre', 'socio')

class AdminProveedor(admin.ModelAdmin):
    list_display = ('dni', 'nombre')
    list_filter = ('dni', 'nombre',)

class AdminFactura(admin.ModelAdmin):
    list_display = ('numero', 'fecha', 'tipo')
    list_filter = ('numero', 'fecha', 'tipo')

class AdminProvee(admin.ModelAdmin):
    list_display = ('producto', 'proveedor')
    list_filter = ('producto', 'proveedor')

class AdminVenta(admin.ModelAdmin):
    list_display = ('venta_producto', 'venta_cantidad', 'venta_cliente', 'venta_empleado', 'venta_factura')
    list_filter = ('venta_producto', 'venta_cantidad', 'venta_cliente', 'venta_empleado', 'venta_factura')

admin.site.register(Empleado, AdminEmpleado)
admin.site.register(Categoria, AdminCategoria)
admin.site.register(Cliente, AdminCliente)
admin.site.register(Proveedor, AdminProveedor)
admin.site.register(Producto, AdminProducto)
admin.site.register(Factura, AdminFactura)
admin.site.register(Provee, AdminProvee)
admin.site.register(Venta, AdminVenta)