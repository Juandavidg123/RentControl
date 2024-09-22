from django.db import models
from .models import Usuario

class UsuarioBuilder:
    def __init__(self):
        self._nombre = ""
        self._apellido = ""
        self._email = ""
        self._password = ""
        self._cedula = 0
    
    def setNombre(self, nombre):
        self._nombre = nombre
        return self
    
    def setApellido(self, apellido):
        self._apellido = apellido
        return self
    
    def setEmail(self, email):
        self._email = email
        return self 
    
    def setPassword(self, password):
        self._password = password
        return self
    
    def setCedula(self, cedula):
        self._cedula = cedula
        return self
    
    def build(self):
        return Usuario.objects.create(nombre=self._nombre, apellido=self._apellido, email=self._email, password=self._password, cedula=self._cedula)