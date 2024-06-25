from django.shortcuts import render

# Create your views here.
def home (request):
    return render (request, "categorias_produc/index.html")

def repekes (request):
    return render (request, "categorias_produc/index.html")

def inicio (request):
    return render (request, "categorias_produc/index.html")

def indumentaria (request):
    return render (request, "categorias_produc/indumentaria.html")


def calzado (request):
    return render (request, "categorias_produc/calzado.html")


def accesorios (request):
    return render (request, "categorias_produc/accesorios.html")


def coches (request):
    return render (request, "categorias_produc/coches.html")
