from django.urls import path
from .views import inmuebles, crearPropiedad

urlpatterns = [
    path('inmuebles/', inmuebles, name='inmuebles'),
    path('crearPropiedad/', crearPropiedad, name='crearPropiedad')
]