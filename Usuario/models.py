from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    cedula = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
