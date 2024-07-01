from django.db import models

# CATEGORIAS DE PRODCUTOS.

class Indumentaria(models.Model):
    nombre=models.CharField(max_length=80)
    marca=models.CharField(max_length=60)
    talle=models.IntegerField()
    precio=models.IntegerField()
    


class Calzado(models.Model):
    nombre=models.CharField(max_length=80)
    marca=models.CharField(max_length=60)
    talle=models.IntegerField()
    precio=models.IntegerField()


class Coches(models.Model):
    nombre=models.CharField(max_length=80)
    marca=models.CharField(max_length=60)
    descripcion=models.CharField(max_length=200)
    precio=models.IntegerField()
   

class Accesorios(models.Model):
    nombre=models.CharField(max_length=80)
    marca=models.CharField(max_length=60)
    descripcion=models.CharField(max_length=200)
    precio=models.IntegerField()