from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    imagen = models.ImageField(upload_to='usuarios', default='default-user.png')
    tipo_usuario = models.CharField(max_length=11, choices=[('publico', 'Publico'), ('colaborador', 'Colaborador')], default='publico')
    pass

# Create your models here.

