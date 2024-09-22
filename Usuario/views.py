from django.shortcuts import render
from .forms import createUserForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import Usuario
from .UsuarioBuilder import UsuarioBuilder


# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form': createUserForm()
        })
    else:
        try:
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            email = request.POST['email']
            password = request.POST['password']
            cedula = request.POST['cedula']

            builder = UsuarioBuilder()
            usuario = builder.setNombre(nombre).setApellido(apellido).setEmail(email).setPassword(password).setCedula(cedula).build()
            usuario.save()
            
            return redirect('inmuebles')

        except Exception as e:
            return render(request, 'signup.html',{
                    'form': createUserForm(),
                    'error': e
            })


def inmuebles(request):
    return render(request, 'inmuebles.html')