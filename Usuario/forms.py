from django import forms
from .models import Usuario

class createUserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'password', 'cedula']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write a task title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write a task description'
            }),
            'important': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'border: 1px solid black'
            })
        }
