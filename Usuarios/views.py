from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .usuarioBuilder import usuarioBuilder

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form': UserCreationForm()
        })
    else:
        try:
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            username = request.POST['username']

            if password1 == password2:
                usuario = usuarioBuilder()
                user = usuario.set_username(username).set_password(password1).build()
                user.save()
                login(request, user)
                return redirect('inmuebles')

            else:
                return render(request, 'signup.html',{
                    'form': UserCreationForm(),
                    'error': 'Passwords do not match'
                })
        except:
            return render(request, 'signup.html',{
                    'form': UserCreationForm(),
                    'error': 'User already exists'
            })
        
@login_required     
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form': AuthenticationForm()
        })
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('inmuebles')
        else:
            return render(request, 'signin.html',{
                'form': AuthenticationForm(),
                'error': 'Usuario o contraseña incorrecta'
            })