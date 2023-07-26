from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre,self.apellido


