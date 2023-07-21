from django.contrib import admin
from .models import Articulo, Categoria, Comentario
# Register your models here.

admin.site.register(Articulo)
admin.site.register(Categoria)
admin.site.register(Comentario)