from django.db import models

# Create your models here.

"""
En esta pestaña van todas las tablas que vamos a hacer, cada una con su clase
para relaciones uno a muchos, se usa ForeignKey
para relaciones muchos a muchos, se usa ManyToManyField
esto solo es necesarion hacerlo en una de las clases
Después en admin.py se hace el registro de cada tabla
"""

class Empleado(models.Model):
    """
    empleados tiene los atributos: dni como clave primaria,
    nombre y codigo como clave foranea(valor entero entre 1 y 3) 
    """
    dni = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    codigo = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    telefono = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    """
    categorias tiene los atributos: codigo como clave primaria,
    nombre 
    """
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    """
    Cliente tiene clave primaria dni, nombre, direccion
    y socio (valor booleano)
    """
    dni = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    socio = models.BooleanField()
    telefono = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    """
    proveedor tiene clave primaria dni, nombre, direccion
    """
    dni = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    """
    producto tiene clave primaria codigo, nombre, precio y stock
    """
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Factura(models.Model):
    """
    Factura tiene clave primaria numero, fecha, tipo (A, B, C o D)
    """
    numero = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    tipo = models.CharField(max_length=1)
    
    def __str__(self):
        return f'{self.numero}---{self.fecha}---{self.tipo}'
    
class Venta(models.Model):
    """
    Esta clase relaciona un Cliente, un Empleado, un Producto y una Factura. Ademas tiene un atributo cantidad
    
    """
    venta_cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True)
    venta_empleado = models.ForeignKey('Empleado', on_delete=models.SET_NULL, null=True)
    venta_producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)
    venta_factura = models.ForeignKey('Factura', on_delete=models.SET_NULL, null=True)
    venta_cantidad = models.IntegerField()
    
    def __str__(self):
        return f'N° {self.venta_factura}---Cliente {self.venta_cliente}--- Producto {self.venta_producto}'
    
class Provee(models.Model):
    """
    Provee relaciona un proveedor con un producto. Además tiene un atributo cantidad
    """
    proveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f'{self.proveedor}---{self.producto}---{self.cantidad}'
