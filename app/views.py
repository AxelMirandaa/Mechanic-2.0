from django.shortcuts import render, redirect, get_object_or_404
from .models import Servicio
from .forms import ServicioForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'app/index.html')

def servicios(request):

    servicios = Servicio.objects.all()
    data = {
        'servicios':servicios
    }

    return render(request,'app/servicios.html',data)

def agregar(request):

    data = {
        'form': ServicioForm()
    }

    if(request.method == 'POST'):
        formulario = ServicioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Servicio agregado correctamente")
        else:
            data["form"] = formulario

    return render(request,'app/agregar.html', data)


def listar(request):
    servicios = Servicio.objects.all()
    data = {
        'servicios': servicios
    }
    return render(request,'app/listar.html', data)


def modificar(request, id):

    servicio = get_object_or_404(Servicio, nombre_servicio=id)

    data = {
        'form':ServicioForm(instance=servicio)
    }

    if(request.method == 'POST'):
        formulario = ServicioForm(request.POST, instance=servicio)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Servicio modificado correctamente")
            return redirect(to="listar")
        else:
            data["form"] = formulario

    return render(request,'app/modificar.html',data)



def eliminar(request, id):
    servicio = get_object_or_404(Servicio,nombre_servicio=id)
    servicio.delete()
    messages.success(request,"Servicio eliminado correctamente")
    return redirect(to="listar")

