from django.urls import path
from .views import inmuebles

urlpatterns = [
    path('inmuebles/', inmuebles, name='inmuebles')
]