from django.db import models
from apps.usuarios.models import Usuario


class Categoria(models.Model):
    nombre = models.CharField(max_length = 30)


    def __str__(self):
        return self.nombre
 
class Noticia(models.Model):
    titulo = models.CharField(max_length = 50)
    resumen = models.CharField(max_length = 100, null = True)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to = 'noticias')
    categoria_noticia = models.ForeignKey(Categoria, on_delete = models.CASCADE) #la otra opcion a CASCADE = SET_NULL
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=Usuario.objects.get(is_superuser=True).pk)
    def __str__(self):
        return self.titulo

class Comment(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text
