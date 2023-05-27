from django import forms 
from . import models

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"
        widgets = {
            'documento' : forms.TextInput(attrs={"class" : "form-control"}),
            'telefono' : forms.TextInput(attrs={"class" : "form-control"}),
            'ap' : forms.TextInput(attrs={"class" : "form-control"}),
            'am' : forms.TextInput(attrs={"class" : "form-control"}),
            'nombre' : forms.TextInput(attrs={"class" : "form-control"}),
            'tipo' : forms.Select(attrs={"class" : "form-control"})
        }
        labels = {
            'ap' : 'Apellido Paterno',
            'am' : 'Apellido Paterno'
        }

class MarcaForm(forms.ModelForm):
    class Meta:
        model = models.Marca
        fields = "__all__"
        widgets = {
            'marca' : forms.TextInput(attrs={"class" : "form-control"})
        }
        labels = {
            'marca' : 'Marca'
        }

class ModeloForm(forms.ModelForm):
    class Meta:
        model = models.Modelo
        fields = "__all__"
        widgets = {
            'modelo' : forms.TextInput(attrs={"class" : "form-control"}),
            'marca' : forms.TextInput(attrs={"class" : "form-control"})
        }
        labels = {
            'marca' : 'Modelo',
            'marca' : 'Marca'
        }