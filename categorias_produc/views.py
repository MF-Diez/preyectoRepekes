from django.shortcuts import render
from categorias_produc.models import *

from .forms import *

# views de HOME.
def home (request):
    return render (request, "categorias_produc/index.html")

def repekes (request):
    return render (request, "categorias_produc/index.html")

def inicio (request):
    return render (request, "categorias_produc/index.html")

# views de categoria INDUMENTARIA.
def indumentaria (request):
    contexto = {"indumentaria": Indumentaria.objects.all()}
    return render (request, "categorias_produc/indumentaria.html",contexto)

def indumentariaForm (request):
    if request.method == "POST":
        miForm = IndumentariaForm(request.POST)
        if miForm.is_valid():
            indumentariaNombre = miForm.cleaned_data.get("nombre")
            indumentariaMarca = miForm.cleaned_data.get("marca")
            indumentariaTalle = miForm.cleaned_data.get("talle")
            indumentariaPrecio = miForm.cleaned_data.get("precio")
            indumentaria = Indumentaria(nombre=indumentariaNombre, marca=indumentariaMarca, talle=indumentariaTalle, precio=indumentariaPrecio)
            indumentaria.save()
            contexto = {"indumentaria": Indumentaria.objects.all()}
            return render (request, "categorias_produc/indumentaria.html",contexto)
    else:
        miForm = IndumentariaForm()
        
    return render (request, "categorias_produc/indumentariaForm.html", {"form": miForm})

def buscarIndumentaria(request):
    return render(request, "categorias_produc/buscarIndumentaria.html")

def encontrarIndumentaria(request):
    if request.GET["buscarInd"]:
        patron= request.GET["buscarInd"]
        indumentaria= Indumentaria.objects.filter(nombre__icontains=patron)
        contexto={"indumentaria": indumentaria}
    else:
        contexto = {"indumentaria": Indumentaria.objects.all()}
        
    return render (request, "categorias_produc/indumentaria.html",contexto)



# views de categoria CALZADO.
def calzado (request):
    contexto = {"calzado": Calzado.objects.all()}
    return render (request, "categorias_produc/calzado.html", contexto)

def calzadoForm (request):
    if request.method == "POST":
        miForm = CalzadoForm(request.POST)
        if miForm.is_valid():
            calzadoNombre = miForm.cleaned_data.get("nombre")
            calzadoMarca = miForm.cleaned_data.get("marca")
            calzadoTalle = miForm.cleaned_data.get("talle")
            calzadoPrecio = miForm.cleaned_data.get("precio")
            calzado = Calzado (nombre=calzadoNombre, marca=calzadoMarca, talle=calzadoTalle, precio=calzadoPrecio)
            calzado.save()
            contexto = {"calzado": Calzado.objects.all()}
            return render (request, "categorias_produc/calzado.html",contexto)
    else:
        miForm = CalzadoForm()
        
    return render (request, "categorias_produc/calzadoForm.html", {"form": miForm})



# views de categoria ACCESORIOS.
def accesorios (request):
    contexto = {"accesorios": Accesorios.objects.all()}
    return render (request, "categorias_produc/accesorios.html", contexto)

def accesorioForm (request):
    if request.method == "POST":
        miForm = AccesoriosForm(request.POST)
        if miForm.is_valid():
            accesorioNombre = miForm.cleaned_data.get("nombre")
            accesorioMarca = miForm.cleaned_data.get("marca")
            accesorioDescripcion = miForm.cleaned_data.get("descripcion")
            accesorioPrecio = miForm.cleaned_data.get("precio")
            accesorio = Accesorios (nombre=accesorioNombre, marca=accesorioMarca, descripcion=accesorioDescripcion, precio=accesorioPrecio)
            accesorio.save()
            contexto = {"accesorios": Accesorios.objects.all()}
            return render (request, "categorias_produc/accesorios.html",contexto)
    else:
        miForm = AccesoriosForm()
        
    return render (request, "categorias_produc/accesoriosForm.html", {"form": miForm})

# views de categoria COCHES.
def coches (request):
    contexto = {"coches": Coches.objects.all()}
    return render (request, "categorias_produc/coches.html", contexto)

def cochesForm (request):
    if request.method == "POST":
        miForm = CochesForm(request.POST)
        if miForm.is_valid():
            cocheNombre = miForm.cleaned_data.get("nombre")
            cocheMarca = miForm.cleaned_data.get("marca")
            cocheDescripcion = miForm.cleaned_data.get("descripcion")
            cochePrecio = miForm.cleaned_data.get("precio")
            coche = Coches (nombre=cocheNombre, marca=cocheMarca, descripcion=cocheDescripcion, precio=cochePrecio)
            coche.save()
            contexto = {"coches": Coches.objects.all()}
            return render (request, "categorias_produc/coches.html",contexto)
    else:
        miForm = CochesForm()
        
    return render (request, "categorias_produc/cochesForm.html", {"form": miForm})
