from django.db import models

# Create your models here.
class Empleado(models.Model):
    Apellido = models.CharField(max_length=30)
    Nombre = models.CharField(max_length=30)
    Dni = models.CharField(max_length=8)