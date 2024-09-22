from django.urls import path
from .views import inmuebles, signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('inmuebles/', inmuebles, name='inmuebles'),
]
