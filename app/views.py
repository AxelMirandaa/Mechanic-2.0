from django.shortcuts import render, redirect, get_object_or_404
from .models import Servicio
from .forms import ServicioForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def home(request):
    return render(request,'app/index.html')

def servicios(request):

    servicios = Servicio.objects.all()
    data = {
        'servicios':servicios
    }

    return render(request,'app/servicios.html',data)

@permission_required('app.add_servicio')
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

@permission_required('app.view_servicio')
def listar(request):
    servicios = Servicio.objects.all()
    data = {
        'servicios': servicios
    }
    return render(request,'app/listar.html', data)

@permission_required('app.change_servicio')
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


@permission_required('app.delete_servicio')
def eliminar(request, id):
    servicio = get_object_or_404(Servicio,nombre_servicio=id)
    servicio.delete()
    messages.success(request,"Servicio eliminado correctamente")
    return redirect(to="listar")

def registro(request):
    data = {
        'form':CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data['username'], password = formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Te has registrado correctamente')
            return redirect(to='home')
        data['form'] = formulario
    return render(request,'registration/registro.html',data)

