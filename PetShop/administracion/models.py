from email.charset import Charset
from pickle import TRUE
from django.db import models

# Create your models here.
class Empleados(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField(unique=True)

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    categoria = models.CharField(max_length=10)
    barcode = models.IntegerField(unique=True)
    precio = models.FloatField()
    stock = models.IntegerField()

class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    contacto_mail = models.CharField(max_length=40)
    contacto_tel = models.CharField(max_length=30)
    