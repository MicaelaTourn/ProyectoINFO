from django.shortcuts import render
from .models import Articulo

# Create your views here.

""" Funcion para mostrar articulos """
def listarArticulos(request):
    articulos = Articulo.objects.all()

    contexto = {
        'articulos': articulos,        
    }
    return render(request, 'articulos/listarArticulos.html',contexto)
