#es una clase que tiene la información que llevará uno o  más formularios en un template
from pyexpat import model
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'cantidad', 'descripcion', 'categoria','imagen']
        labels = {
            'id' : "Id",
            'nombre' : "Nombre",
            'precio' : "Precio",
            'cantidad': "Cantidad",
            'descripcion' : "Descripcion",
            'categoria' : "Categoria",
            'imagen': "Imagen",
        }
        widgets={
            'id' : forms.TextInput(
                attrs={
                    'placeholder' : 'ID de producto',
                    'class' : 'form-control',
                    'id' : 'id'
                }
            ),
            'nombre' : forms.TextInput(
                attrs={
                    'placeholder' : 'Nombre de producto',
                    'class' : 'form-control',
                    'id' : 'nombre'
                }
            ),
            'precio':forms.TextInput(
                attrs={
                    'placeholder' : 'Precio del producto',
                    'class' : 'form-control',
                    'id' : 'precio'
                }
            ),
            'cantidad':forms.TextInput(
                attrs={
                    'placeholder' : 'Cantidad en inventario',
                    'class' : 'form-control',
                    'id' : 'cantidad'
                }
            ),
            'descripcion':forms.TextInput(
                attrs={
                    'placeholder' : 'Descripción del producto',
                    'class' : 'form-control',
                    'id' : 'modelo'
                }
            ),
            'categoria':forms.Select(
                attrs={
                    'class' : 'form-control',
                    'id' : 'categoria'
                }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'class' : 'form-control',
                    'id' : 'imagen'
                }
            )
        }