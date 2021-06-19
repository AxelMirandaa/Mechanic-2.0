
from django.urls import path

from .views import home, servicios, agregar, modificar, listar, eliminar


urlpatterns = [

    path('',home,name='home'),
    path('servicios/', servicios, name='servicios'),
    path('agregar/', agregar, name='agregar'),
    path('modificar/<id>/', modificar, name='modificar'),
    path('listar/', listar, name='listar'),
    path('eliminar/<id>', eliminar, name='eliminar'),

]