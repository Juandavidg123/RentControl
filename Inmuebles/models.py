from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Propiedades(models.Model):
    tipo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    numeroDeInquilinos = models.IntegerField()
    inquilino = models.ForeignKey(User, on_delete=models.CASCADE)

class Arrendado(models.Model):
    fechaInicio = models.DateField(auto_now_add=True)
    monto = models.FloatField()
    pagado = models.BooleanField(default=False)
    dueño = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.propiedad.tipo