from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name= "home" ),
    path('inicio/', inicio, name= "index" ),
    path('repekes/', repekes, name= "index" ),
    path('indumentaria/', indumentaria, name= "indumentaria" ),
    path('indumentaria/', indumentaria, name= "indumentaria" ),
    path('calzado/', calzado, name= "calzado" ),
    path('accesorios/', accesorios, name= "accesorios" ),
    path('coches/', coches, name= "coches" ),
]
