from django import forms


class Empleado_formulario(forms.Form):

    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    dni= forms.IntegerField()

class Producto_formulario(forms.Form):

    nombre_producto = forms.CharField(max_length=100)
    categoria = forms.CharField(max_length=10)
    barcode = forms.IntegerField()
    precio = forms.FloatField()
    stock = forms.IntegerField()


class Cliente_formulario(forms.Form):
    
    nombre= forms.CharField(max_length=40)
    contacto_mail= forms.CharField(max_length=40)
    contacto_tel= forms.CharField(max_length=30)