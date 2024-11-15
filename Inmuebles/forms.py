from .models import Propiedades
from django import forms

class PropiedadesForm(forms.ModelForm):
    class Meta:
        model = Propiedades
        fields = ['tipo', 'direccion', 'numeroDeInquilinos', 'inquilino']  
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'numeroDeInquilinos': forms.NumberInput(attrs={'class': 'form-control'}),
            'inquilino': forms.Select(attrs={'class': 'form-control'}),
        }
