from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Empleado, Categoria, Cliente, Proveedor, Producto, Factura, Provee, Venta
from .forms import FormEmpleado, FormCliente, FormProveedor, FormProdcuctos, FormFactura, FormVentas, FormPrimeraVenta, FormProvee
import datetime

# Create your views here.

def index(request):
    return render(request, 'pagina_shell/home.html')

def carga_exitosa(request):
    return render(request, 'pagina_shell/carga_exitosa.html')

def lista_empleados(request):
    empleados = Empleado.objects.all()
    if request.method == 'POST':
        form = FormEmpleado(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/carga_exitosa/')
    else:
        form = FormEmpleado()

    return render(request, 'pagina_shell/vista_empleados.html', {
        'empleados': empleados,
        'form': form
        })

def lista_ventas_por_empleado(request, dni):
    empleado = Empleado.objects.get(dni=dni)
    ventas = Venta.objects.filter(venta_empleado=empleado)
    total_ventas = 0
    for venta in ventas:
        total_ventas += venta.venta_cantidad * venta.venta_producto.precio
    return render(request, 'pagina_shell/vista_venta_por_empleado.html', {
        'ventas': ventas,
        'empleado': empleado,
        'total_venta': total_ventas
    })

def lista_clientes(request):
    clientes = Cliente.objects.all()
    if request.method == 'POST':
        form = FormCliente(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/carga_exitosa/')
    else:
        form = FormCliente()
    return render(request, 'pagina_shell/vista_clientes.html', {
        'clientes': clientes,
        'form': form
    })
        
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    if request.method == 'POST':
        form = FormProveedor(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/carga_exitosa/')
    else:
        form = FormProveedor()
    return render(request, 'pagina_shell/vista_proveedores.html', {
        'proveedores': proveedores,
        'form': form
    })
    
def lista_productos(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        form = FormProdcuctos(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/carga_exitosa/')
    else:
        form = FormProdcuctos()
    return render(request, 'pagina_shell/vista_productos.html', {
        'productos': productos,
        'form': form
    })

def lista_facturas(request):
    facturas = Factura.objects.all()
    if request.method == 'POST':
        form = FormFactura(request.POST)
        
        if form.is_valid():
            factura = Factura(
                numero = len(facturas)+1,
                fecha = form.cleaned_data['fecha'],
                tipo = form.cleaned_data['tipo'],
            )
            factura.save()
            return HttpResponseRedirect('/carga_exitosa/')
    else:
        form = FormFactura()
    return render(request, 'pagina_shell/vista_facturas.html', {
        'facturas': facturas,
        'form': form
    })

def lista_ventas(request, numero):

    factura = Factura.objects.get(numero=numero)
    ventas = Venta.objects.filter(venta_factura=factura)
    if len(ventas) == 0:
        empleado, cliente = None, None
        form = FormPrimeraVenta()
        precio_total = 0
    else:
        precio_total = 0
        for venta in ventas:
            precio_total += venta.venta_producto.precio * venta.venta_cantidad
        form = FormVentas()
        empleado = ventas[0].venta_empleado
        cliente = ventas[0].venta_cliente
    if request.method == 'POST':
        if len(ventas) == 0:
            form = FormPrimeraVenta(request.POST)
        else:
            form = FormVentas(request.POST)
        
        if form.is_valid():
            try:
                venta = Venta(
                    venta_factura = factura,
                    venta_empleado = form.cleaned_data['empleado'],
                    venta_cliente = form.cleaned_data['cliente'],
                    venta_producto = form.cleaned_data['producto'],
                    venta_cantidad = form.cleaned_data['cantidad'],
                )
            except KeyError:
                venta = Venta(
                    venta_factura = factura,
                    venta_empleado = empleado,
                    venta_cliente = cliente,
                    venta_producto = form.cleaned_data['producto'],
                    venta_cantidad = form.cleaned_data['cantidad'],
                )
            venta.save()
            return HttpResponseRedirect('/carga_exitosa/')
    return render(request, 'pagina_shell/vista_ventas.html', {
        'ventas': ventas,
        'form': form,
        'factura': factura,
        'empleado': empleado,
        'cliente': cliente,
        'precio_total': precio_total,
    })

def lista_provee(request, numero):

    provee = Provee.objects.filter(proveedor=numero)
    proveedor = Proveedor.objects.get(dni=numero)
    if request.method == 'POST':
        form = FormProvee(request.POST)
        
        if form.is_valid():
            provee = Provee(
                proveedor = proveedor,
                producto = form.cleaned_data['producto'],
                cantidad = form.cleaned_data['cantidad'],
            )
            provee.save()
            return HttpResponseRedirect('/carga_exitosa/')
    else:
        form = FormProvee()

    return render(request, 'pagina_shell/vista_provee.html', {
        'provee': provee,
        'proveedor': proveedor,
        'form': form,
    })

def facturas_B(request):
    """
    Esta función lista todos los clientes que hayan requerido alguna factura de tipo B
    """
    ventas = Venta.objects.filter(venta_factura__tipo='B')
    clientes = []
    for venta in ventas:
        if venta.venta_cliente not in clientes:
            clientes.append(venta.venta_cliente)
    return render(request, 'pagina_shell/facturas_b.html',{
                  'clientes': clientes
                  })

def ventas_uno(request):

    """
    Esta función lista los productos vendidos por los empleados de tipo 1
    """
    ventas = Venta.objects.filter(venta_empleado__codigo=1)
    productos = []
    for venta in ventas:
        if venta.venta_producto not in productos:
            productos.append(venta.venta_producto)
    return render(request, 'pagina_shell/tipo_uno.html',{
                    'productos': productos
                    })

def provisto_por(request, codigo):
    """
    Dado un codigo de producto, lista los proveedores que lo proveen
    """
    producto = Producto.objects.get(codigo=codigo)
    proveedores = []
    provee = Provee.objects.filter(producto=producto)
    for prove in provee:
        if prove.proveedor not in proveedores:
            proveedores.append(prove.proveedor)
    return render(request, 'pagina_shell/vista_producto_por_codigo.html',{
                    'proveedores': proveedores,
                    'producto': producto
                    })