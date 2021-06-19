from django import forms
from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Servicio

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'
        

