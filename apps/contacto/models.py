from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    telefono = models.CharField( max_length=20)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.nombre
