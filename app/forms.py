from django import forms
from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Servicio
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email','password1','password2']



