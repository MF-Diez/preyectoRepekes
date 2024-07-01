from django.shortcuts import render
from categorias_produc.models import *


# Create your views here.
def home (request):
    return render (request, "categorias_produc/index.html")

def repekes (request):
    return render (request, "categorias_produc/index.html")

def inicio (request):
    return render (request, "categorias_produc/index.html")


def indumentaria (request):
    contexto = {"indumentaria": Indumentaria.objects.all()}
    return render (request, "categorias_produc/indumentaria.html",contexto)


def calzado (request):
    contexto = {"calzado": Calzado.objects.all()}
    return render (request, "categorias_produc/calzado.html", contexto)


def accesorios (request):
    contexto = {"accesorios": Accesorios.objects.all()}
    return render (request, "categorias_produc/accesorios.html", contexto)


def coches (request):
    contexto = {"coches": Coches.objects.all()}
    return render (request, "categorias_produc/coches.html", contexto)
