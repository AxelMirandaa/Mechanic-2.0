from django.contrib import admin
from .models import Vehiculo, TipoVehiculo, Servicio

# Register your models here.

admin.site.register(Vehiculo)
admin.site.register(TipoVehiculo)
admin.site.register(Servicio)

