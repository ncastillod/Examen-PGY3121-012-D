from django.urls import path
from .views import *

urlpatterns=[ 
    path('', inicio, name="inicio"),

    path('gestion/', gestion, name="gestion"),

    path('qsomos/', qsomos, name="qsomos"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('registrar/', registrar, name="registrar"),
    path('productos/', productos, name="productos"),
    path('contactanos/', contactanos, name="contactanos"),
    path('carrito/', carrito, name="carrito"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('agregarpr/<id>', agregar_productopr, name="agregarpr"),
    path('eliminarcarrito/<id>', eliminar_producto, name="eliminarcarrito"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
    path('registrar/', registrar, name="registrar"),
    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    
]