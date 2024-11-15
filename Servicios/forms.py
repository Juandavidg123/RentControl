from .models import Servicios
from django import forms

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = ['montoAgua', 'montoLuz', 'montoGas', 'pagadoAgua', 'pagadoLuz', 'pagadoGas']
        widgtets = {
            'montoAgua': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Monto de agua'
                }),
            'montoLuz': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Monto de luz'
                }),
            'montoGas': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Monto de gas'
                }),
            'pagadoAgua': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                }),
            'pagadoLuz': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                }),
            'pagadoGas': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                }),
        }
        labels = {
            'montoAgua': 'Monto de agua',
            'montoLuz': 'Monto de luz',
            'montoGas': 'Monto de gas',
            'pagadoAgua': '¿Pagado Agua?',
            'pagadoLuz': '¿Pagado Luz?',
            'pagadoGas': '¿Pagado Gas?',
        }