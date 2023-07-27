from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.
# definimos clase categoria 
class Categoria(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):       
            return self.descripcion

# definimos clase articulo
class Articulo(models.Model):
    titulo = models.CharField(max_length=250)
    contenido_breve = models.CharField(max_length=500)
    contenido_completo = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='articulos')
    categoria_articulo = models.ForeignKey(Categoria, on_delete=models.SET_NULL,null=True,default='Sin categoría')
    usuario_articulo = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

# definimos clase comentario
class Comentario(models.Model):
    articulo_comentario = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='comentarios')
    usuario_comentario = models.CharField(max_length=100)
    comentario = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.comentario