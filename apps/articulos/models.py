from django.db import models

# Create your models here.
class Categoria(models.Model):
    description = models.CharField(max_length=200)
    activo = models.BooleanField()

    def __str__(self):
        return self.description
    