from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Propiedades(models.Model):
    tipo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    numeroDeInquilinos = models.IntegerField()
    dueño = models.ForeignKey(User, related_name="dueño_propiedades", on_delete=models.CASCADE)
    inquilino = models.ForeignKey(User, related_name='dueñoInquilino',on_delete=models.CASCADE)
