from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    telefono= models.IntegerField(max_length=20)
    fecha_nacimiento=models.DateField()