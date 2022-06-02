from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    contraseña = models.CharField(max_length=20)
    
    
    
    
class Textos(models.Model):
    nombre = models.CharField(max_length=40)
    texto = models.TextField()


class Personas(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=20)
    edad = models.IntegerField()
    
