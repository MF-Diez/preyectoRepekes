from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name= "home" ),
    path('inicio/', inicio, name= "index" ),
    path('repekes/', repekes, name= "index" ),
    
    path('cargarProductosForm/', indumentariaForm, name= "indumentariaForm" ),
    
#___Categoria Indumentaria    
    path('indumentaria/', indumentaria, name= "indumentaria" ),
    path('cargarProductosForm/', indumentariaForm, name= "indumentariaForm" ),

#___Categoria Calzado     
    path('calzado/', calzado, name= "calzado" ),
    path('cargarProductosForm/', calzadoForm, name= "calzadoForm" ),
    
#___Categoria Accesorios     
    path('accesorios/', accesorios, name= "accesorios" ),
    path('cargarProductosForm/', accesorioForm, name= "accesoriosForm" ),
    
#___Categoria Coches     
    path('coches/', coches, name= "coches" ),
    path('cargarProductosForm/', cochesForm, name= "cochesForm" ),
]
