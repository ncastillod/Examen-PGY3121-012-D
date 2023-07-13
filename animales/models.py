from tabnanny import verbose
from django.db import models
import datetime

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de Categoria")
    nombreCategoria= models.CharField(max_length=50, blank=True, verbose_name="Nombre de Categoria")


    def __str__(self):
        return self.nombreCategoria
    
class Producto(models.Model):
    id= models.CharField(primary_key=True, max_length=2, verbose_name="Id")
    nombre= models.CharField(max_length=50, blank=True, verbose_name="Nombre")
    precio= models.IntegerField(default=0,blank=True, verbose_name="Precio")
    cantidad= models.IntegerField(default=0, blank=True, verbose_name="Cantidad")
    descripcion= models.CharField(max_length=200, blank=True, verbose_name="Descripcion")    
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    imagen=models.ImageField(upload_to="imagenes",null=True, blank=True,verbose_name="Imagen")

    def __str__(self):
        return self.id
    
class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
    estado = models.CharField(max_length=15, blank=True, verbose_name="Estado")

    def str(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    usuario = models.CharField(max_length=100, blank=True, verbose_name="Usuario")
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def str(self):
        return str(self.id_detalle_boleta)