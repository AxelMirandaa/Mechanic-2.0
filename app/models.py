from django.db import models

# Create your models here.
class TipoVehiculo(models.Model):

    id_tipo = models.AutoField(primary_key=True, verbose_name='Id tipo')
    nombre_tipo = models.CharField(max_length=50, verbose_name='Tipo de vehiculo')

    def __str__(self):
        return self.nombreTipo


class Vehiculo(models.Model):
    marca = models.CharField(max_length=25, primary_key=True, verbose_name='Marca')
    annio = models.IntegerField( null=True, blank=True, verbose_name='Año')
    tipo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE)


    def __str__(self):
        return self.marca

class Servicio(models.Model):
    nombre_servicio= models.CharField(max_length=25, primary_key=True,verbose_name='Nombre Servicio')
    precio = models.IntegerField(verbose_name = 'Precio')
    descripcion = models.CharField(max_length=250)
    duracion = models.IntegerField() 

    def __str__(self):
        return self.nombre_servicio