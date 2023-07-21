from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Articulo, Categoria, Comentario
from .forms import ArticuloForm, CategoriaForm

# Create your views here.

# Funcion para mostrar articulos
def listarArticulos(request):
    articulos = Articulo.objects.all()

    contexto = {
        'articulos': articulos,        
    }
    return render(request, 'articulos/listarArticulos.html',contexto)


# CREAR ARTICULO
@login_required
def AddArticulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES) ##REQUEST FILE PARA LAS IMAGENES
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.usuario_articulo = request.user #autor de la noticia
            articulo.save()
            return redirect('home')
    else:
        form =ArticuloForm()
    
    return render(request, 'articulos/addArticulo.html', {'form': form})

# CREAR CATEGORIA
@login_required
def  addCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES) ##REQUEST FILE PARA LAS IMAGENES
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.save()
            return redirect('home')
    else:
        form =CategoriaForm()
    
    return render(request, 'articulos/addCategoria.html', {'form': form})