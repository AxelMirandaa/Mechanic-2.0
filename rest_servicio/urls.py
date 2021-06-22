from django.urls import path
from rest_servicio.views import lista_servicios

urlpatterns = [
    
    path('lista_servicios',lista_servicios,name='lista_servicios'),
]

