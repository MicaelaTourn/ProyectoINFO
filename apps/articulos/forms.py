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

# FORMULARIO DE COMENTARIO
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario']
        exclude = ['usuario_comentario']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ComentarioForm,self).__init__(*args, **kwargs)
        if user:
            self.instance.usuario_comentario = user.username