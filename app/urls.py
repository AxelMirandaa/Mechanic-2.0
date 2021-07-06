
from django.urls import path

from .views import home, registro, servicios, agregar, modificar, listar, eliminar, registro, serviciosApi


urlpatterns = [

    path('',home,name='home'),
    path('servicios/', servicios, name='servicios'),
    path('serviciosApi/', serviciosApi, name='serviciosApi'),
    path('agregar/', agregar, name='agregar'),
    path('modificar/<id>/', modificar, name='modificar'),
    path('listar/', listar, name='listar'),
    path('eliminar/<id>', eliminar, name='eliminar'),
    path('registro',registro,name='registro'),
    

]