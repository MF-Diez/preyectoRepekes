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
        miForm1 = IndumentariaForm(request.POST)
        if miForm1.is_valid():
            indumentariaNombre = miForm1.cleaned_data.get("nombre")
            indumentariaMarca = miForm1.cleaned_data.get("marca")
            indumentariaTalle = miForm1.cleaned_data.get("talle")
            indumentariaPrecio = miForm1.cleaned_data.get("precio")
            indumentaria = Indumentaria(nombre=indumentariaNombre, marca=indumentariaMarca, talle=indumentariaTalle, precio=indumentariaPrecio)
            indumentaria.save()
            contexto = {"indumentaria": Indumentaria.objects.all()}
            return render (request, "categorias_produc/indumentaria.html",contexto)
    else:
        miForm1 = IndumentariaForm()
        
    return render (request, "categorias_produc/cargarProductosForm.html", {"form": miForm1})


# views de categoria CALZADO.
def calzado (request):
    contexto = {"calzado": Calzado.objects.all()}
    return render (request, "categorias_produc/calzado.html", contexto)

def calzadoForm (request):
    if request.method == "POST":
        miForm2 = CalzadoForm(request.POST)
        if miForm2.is_valid():
            calzadoNombre = miForm2.cleaned_data.get("nombre")
            calzadoMarca = miForm2.cleaned_data.get("marca")
            calzadoTalle = miForm2.cleaned_data.get("talle")
            calzadoPrecio = miForm2.cleaned_data.get("precio")
            calzado = Calzado (nombre=calzadoNombre, marca=calzadoMarca, talle=calzadoTalle, precio=calzadoPrecio)
            calzado.save()
            contexto = {"calzado": Calzado.objects.all()}
            return render (request, "categorias_produc/calzado.html",contexto)
    else:
        miForm2 = CalzadoForm()
        
    return render (request, "categorias_produc/cargarProductosForm.html", {"form": miForm2})



# views de categoria ACCESORIOS.
def accesorios (request):
    contexto = {"accesorios": Accesorios.objects.all()}
    return render (request, "categorias_produc/accesorios.html", contexto)

def accesorioForm (request):
    if request.method == "POST":
        miForm3 = AccesoriosForm(request.POST)
        if miForm3.is_valid():
            accesorioNombre = miForm3.cleaned_data.get("nombre")
            accesorioMarca = miForm3.cleaned_data.get("marca")
            accesorioDescripcion = miForm3.cleaned_data.get("descripcion")
            accesorioPrecio = miForm3.cleaned_data.get("precio")
            accesorio = Accesorios (nombre=accesorioNombre, marca=accesorioMarca, descripcion=accesorioDescripcion, precio=accesorioPrecio)
            accesorio.save()
            contexto = {"accesorio": Accesorios.objects.all()}
            return render (request, "categorias_produc/accesorios.html",contexto)
    else:
        miForm3 = AccesoriosForm()
        
    return render (request, "categorias_produc/cargarProductosForm.html", {"form": miForm3})

# views de categoria COCHES.
def coches (request):
    contexto = {"coches": Coches.objects.all()}
    return render (request, "categorias_produc/coches.html", contexto)

def cochesForm (request):
    if request.method == "POST":
        miForm4 = CochesForm(request.POST)
        if miForm4.is_valid():
            cocheNombre = miForm4.cleaned_data.get("nombre")
            cocheMarca = miForm4.cleaned_data.get("marca")
            cocheDescripcion = miForm4.cleaned_data.get("descripcion")
            cochePrecio = miForm4.cleaned_data.get("precio")
            coche = Accesorios (nombre=cocheNombre, marca=cocheMarca, descripcion=cocheDescripcion, precio=cochePrecio)
            coche.save()
            contexto = {"coche": Coches.objects.all()}
            return render (request, "categorias_produc/coches.html",contexto)
    else:
        miForm4 = CochesForm()
        
    return render (request, "categorias_produc/cargarProductosForm.html", {"form": miForm4})
