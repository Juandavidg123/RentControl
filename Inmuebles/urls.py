from django.urls import path
from .views import inmuebles, crearPropiedad, detailPropiedad, delete, deletePropiedad, updatePropiedad

urlpatterns = [
    path('inmuebles/', inmuebles, name='inmuebles'),
    path('crearPropiedad/', crearPropiedad, name='crearPropiedad'),
    path('detailPropiedad/<int:id>/', detailPropiedad, name='detailPropiedad'),
    path('delete/<int:id>/', delete, name='delete'),
    path('deletePropiedad/<int:id>/', deletePropiedad, name='deletePropiedad'),
    path('updatePropiedad/<int:id>/', updatePropiedad, name='updatePropiedad')
]