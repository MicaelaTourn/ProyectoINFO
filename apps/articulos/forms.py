from django import forms    
from .models import Articulo, Comentario

class ArticuloForm(forms.ModelForm):
    
    class Meta:
        model = Articulo
        fields = ['titulo','contenido_breve','contenido_completo','imagen','categoria_articulo']