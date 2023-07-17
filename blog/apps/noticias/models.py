from django.db import models
 
class Categoria(models.Model):
    nombre = models.CharField(max_length = 30)


    def __str__(self):
        return self.nombre
 
class Noticia(models.Model):
    titulo = models.CharField(max_length = 50)
    resumen = models.CharField(max_length = 100, null = True)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    #imagen requiere la libreria pillow
    imagen = models.ImageField(upload_to = 'noticias')
    categoria_noticia = models.ForeignKey(Categoria, on_delete = models.CASCADE) #la otra opcion a CASCADE = SET_NULL
 
    def __str__(self):
        return self.titulo
