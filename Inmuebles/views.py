from django.shortcuts import render, redirect
from .forms import PropiedadesForm
from django.contrib.auth.decorators import login_required
from .models import Propiedades
from .propiedadBuilder import propiedadBuilder

# Create your views here.

@login_required
def inmuebles(request):
    usuario = request.user
    propiedades_inquilino = Propiedades.objects.filter(inquilino=usuario)
    propiedades_dueño = Propiedades.objects.filter(dueño=usuario)

    context = {
        'propiedades_inquilino': propiedades_inquilino,
        'propiedades_dueño': propiedades_dueño,
    }
    
    return render(request, 'inmuebles.html', context)


@login_required
def crearPropiedad(request):
    if request.method == 'GET':
        return render(request, 'crearPropiedad.html', {
            'form': PropiedadesForm()
            })
    else:
        try:
            propiedad = propiedadBuilder()
            propiedad.set_propiedad(request.POST, request.user).set_save()
            return redirect('inmuebles')
        except:
            return render(request, 'crearPropiedad.html', {
                'form': PropiedadesForm(),
                'error': 'Error al crear la propiedad'
                })