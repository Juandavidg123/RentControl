from django.shortcuts import render, redirect, get_object_or_404
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
        'usuario': usuario
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
            propiedad.set_propiedad(request.POST, request.user).build()
            return redirect('inmuebles')
        except:
            return render(request, 'crearPropiedad.html', {
                'form': PropiedadesForm(),
                'error': 'Error al crear la propiedad'
                })
            
@login_required
def detailPropiedad(request, id):
    propiedad = get_object_or_404(Propiedades, id=id);
    dueño = propiedad.dueño == request.user
    return render(request, 'detailPropiedad.html', {
        'propiedad': propiedad,
        'dueño': dueño
        })

@login_required
def delete(request, id):
    return render(request, 'delete.html', {
        'propiedad': get_object_or_404(Propiedades, pk=id)
    })
    
@login_required
def deletePropiedad(request, id):
    propiedad = get_object_or_404(Propiedades, pk=id)
    propiedad.delete()
    return redirect('inmuebles')

@login_required
def updatePropiedad(request, id):
    propiedad = get_object_or_404(Propiedades, pk=id)
    if request.method == 'GET':
        form = PropiedadesForm(instance=propiedad)
        return render(request, 'update.html', {
            'form': form,
            'propiedad': propiedad
        })
    else:
        try:
            form = PropiedadesForm(request.POST, instance=propiedad)
            form.save()
            return redirect('inmuebles')
        except ValueError:
            return render(request, 'update.html', {
                'form': PropiedadesForm(),
                'propiedad': propiedad,
                'error': 'Error al actualizar la propiedad'
            })