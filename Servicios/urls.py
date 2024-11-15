from django.urls import path
from .views import editarServicio, eliminarServicio

urlpatterns = [
    path('editarServicio/<int:id>/', editarServicio, name='editarServicio'),
    path('eliminarServicio/<int:id>/', eliminarServicio, name='eliminarServicio'),
]