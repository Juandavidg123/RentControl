from django.db import models

# Create your models here.
class Servicios(models.Model):
    montoAgua = models.FloatField()
    montoLuz = models.FloatField()
    montoGas = models.FloatField()
    pagadoAgua = models.BooleanField(default=False)
    pagadoLuz = models.BooleanField(default=False)
    pagadoGas = models.BooleanField(default=False)
    propiedad = models.ForeignKey('Inmuebles.Propiedades', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre