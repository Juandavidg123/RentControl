from django.shortcuts import render, get_object_or_404, redirect
from .forms import ServiciosForm
from .models import Servicios
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def editarServicio(request, id):
    servicio = get_object_or_404(Servicios, id=id)
    
    if request.method == 'POST':
        form = ServiciosForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('detailPropiedad', id=servicio.propiedad.id)
    else:
        form = ServiciosForm(instance=servicio)
    
    return render(request, 'editarServicio.html', {
        'form': form,
        'servicio': servicio
    })

@login_required
def eliminarServicio(request, id):
    servicio = get_object_or_404(Servicios, id=id)
    propiedad_id = servicio.propiedad.id
    servicio.delete()
    return redirect('detailPropiedad', id=propiedad_id)