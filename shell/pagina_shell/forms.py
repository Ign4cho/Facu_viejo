from django import forms
from .models import Empleado, Cliente, Proveedor, Producto, Factura, Provee, Venta
import datetime

class FormEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ('dni', 'nombre', 'telefono','codigo')

class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('dni', 'nombre', 'telefono','direccion','socio')

class FormProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ('dni', 'nombre', 'telefono','direccion')
    

class FormProdcuctos(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo', 'nombre', 'precio','stock')

class FormFactura(forms.Form):
    """
    Priemro se genera la factura, con número, fecha y tipo (A, B, C o D)
    Luego en otro form se agregan los productos a la factura
    """
    tipos = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
    
    fecha = forms.DateField(initial=datetime.date.today)
    tipo = forms.ChoiceField(choices=tipos, initial='A')

class FormPrimeraVenta(forms.Form):
    """
    Se agrega el cliente y empleado a la factura
    """
    producto = forms.ModelChoiceField(queryset=Producto.objects.all())
    cantidad = forms.IntegerField()
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    empleado = forms.ModelChoiceField(queryset=Empleado.objects.all())


class FormVentas(forms.Form):
    """
    Se agregan los productos a la factura
    """
    producto = forms.ModelChoiceField(queryset=Producto.objects.all())
    cantidad = forms.IntegerField()

class FormProvee(forms.Form):
    """
    Se agregan los productos al proveedor
    """
    producto = forms.ModelChoiceField(queryset=Producto.objects.all())
    cantidad = forms.IntegerField()