from django import forms    
from .models import Articulo, Categoria, Comentario

# FORMULARIO DE ARTICULO
class ArticuloForm(forms.ModelForm):
    
    class Meta:
        model = Articulo
        fields = ['titulo','contenido_breve','contenido_completo','imagen','categoria_articulo']

# FORMULARIO DE CATEGORIA
class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['descripcion']
