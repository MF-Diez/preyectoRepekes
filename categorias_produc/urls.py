from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name= "home" ),
    path('inicio/', inicio, name= "index" ),
    path('repekes/', repekes, name= "index" ),
    
    
    
#___Categoria Indumentaria    
    path('indumentaria/', indumentaria, name= "indumentaria" ),
    path('indumentariaForm/', indumentariaForm, name= "indumentariaForm" ),
    path('buscarIndumentaria/', buscarIndumentaria, name= "buscarIndumentaria" ),
    path('encontrarIndumentaria/', encontrarIndumentaria, name= "encontrarIndumentaria" ),


#___Categoria Calzado     
    path('calzado/', calzado, name= "calzado" ),
    path('calzadoForm/', calzadoForm, name= "calzadoForm" ),
    
#___Categoria Accesorios     
    path('accesorios/', accesorios, name= "accesorios" ),
    path('accesoriosForm/', accesorioForm, name= "accesoriosForm" ),
    
#___Categoria Coches     
    path('coches/', coches, name= "coches" ),
    path('cochesForm/', cochesForm, name= "cochesForm" ),
]
