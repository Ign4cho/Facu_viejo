from django.urls import path
from pagina_shell import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('empleados/', views.lista_empleados, name='empleado'),
    path('empleados/<int:dni>/', views.lista_ventas_por_empleado, name='ventas_empleado'),
    path('clientes/', views.lista_clientes, name='cliente'),
    path('proveedores/', views.lista_proveedores, name='proveedor'),
    path('proveedores/<int:numero>/', views.lista_provee, name='productos_proveedor'),
    path('productos/', views.lista_productos, name='producto'),
    path('productos/<int:codigo>/', views.provisto_por, name='producto_codigo'),
    path('facturas/', views.lista_facturas, name='factura'),
    path('facturas/<int:numero>/', views.lista_ventas, name='venta'),
    path('carga_exitosa/', views.carga_exitosa, name='carga_exitosa'),
    path('facturas-b/', views.facturas_B, name='facturas-b'),
    path('ventas-uno/', views.ventas_uno, name='ventas-uno')
]