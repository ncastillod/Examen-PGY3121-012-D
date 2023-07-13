from django.shortcuts import render, redirect
from .models import *
from .forms import ProductoForm, RegistroUserForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from animales.compra import Carrito


# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def qsomos(request):
    return render(request, 'qsomos.html')

def productos(request):
    return render(request, 'productos.html')

def contactanos(request):
    return render(request,'contactanos.html')

def carrito(request):
    precio_total = 0
    carrito = request.session.get('carrito', {})  # Obtener el carrito de la sesión

    for item in carrito.values():
        precio = int(item.get('precio', 0))
        cantidad = int(item.get('cantidad', 0))
        precio_total += precio * cantidad

    return render(request, 'carrito.html', {'precio_total': precio_total})

def registrar(request):
    data ={
        'form' : RegistroUserForm()
    }
    if request.method== "POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente!")
            return redirect('inicio')
        data["form"] = formulario       #sobreescribimos el form
    return render(request, 'registration/registro.html', data)


@login_required
def crear(request):
    if request.method=="POST":
        productoform = ProductoForm(request.POST,request.FILES) #creamos un objeto de tipo form 
        if productoform.is_valid():
            productoform.save() #similar en funcion al metodo insert
            return redirect ('gestion')
    else:
        productoform=ProductoForm()
    return render(request, 'crear.html', {'productoform' : productoform})
    
@login_required
def eliminar(request, id):
    productoEliminado=Producto.objects.get(id=id) #buscamos un  por la ids
    productoEliminado.delete()
    return redirect('gestion')

@login_required
def modificar(request,id):
    productoModificado = Producto.objects.get(id=id)
    datos ={
        'form': ProductoForm(instance=productoModificado)   #el objeto form llega al template
    }
    if request.method=="POST":          #modificamos backend con los cambios realizagestion
        formulario = ProductoForm(request.POST, request.FILES, instance=productoModificado)
        if formulario.is_valid():
            formulario.save()           #modificamos el objeto
            return redirect('gestion')
    return render(request,'modificar.html', datos)





def gestion(request):
    productos=Producto.objects.raw('select * from animales_producto')
    datos={'productos':productos}
    return render(request, 'gestion.html', datos)




def productos(request):
    # Obtener todos los productos
    productos = Producto.objects.all()

    # Configurar el paginador con una cierta cantidad de productos por página
    paginator = Paginator(productos, 9)  # Mostrar 9 productos por página

    # Obtener el número de página actual desde los parámetros de la URL
    page_number = request.GET.get('page')

    # Obtener la página actual del paginador
    page_obj = paginator.get_page(page_number)

    return render(request, 'productos.html', {'productos': page_obj})



def agregar_productopr(request,id):
    carrito_compra = Carrito(request)
    Productos = Producto.objects.get(id=id)
    carrito_compra.agregarpr(Producto=Productos)
    return redirect('productos')


def agregar_producto(request,id):
    carrito_compra = Carrito(request)
    Productos = Producto.objects.get(id=id)
    carrito_compra.agregar(Producto=Productos)
    return redirect('carrito')

def eliminar_producto(request,id):
    carrito_compra = Carrito(request)
    Productos = Producto.objects.get(id=id)
    carrito_compra.eliminar(Producto=Productos)
    return redirect('carrito')

def restar_producto(request,id):
    carrito_compra = Carrito(request)
    Productos = Producto.objects.get(id=id)
    carrito_compra.restar(Producto=Productos)
    return redirect('carrito')

def limpiar_carrito(request):
    carrito_compra = Carrito(request)
    carrito_compra.limpiar()
    return redirect('carrito')


def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total, estado = 'Procesando Pedido')
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(id = value['producto_id'])
            cant = value['cantidad']
            producto.cantidad = producto.cantidad - cant
            producto.save()
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, usuario = request.user.username, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)

