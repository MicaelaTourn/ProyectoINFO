from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Articulo, Categoria, Comentario
from .forms import ArticuloForm, CategoriaForm

# SECCION ARTICULOS

# Funcion para mostrar articulos
def listarArticulos(request):
    articulos = Articulo.objects.all()

    contexto = {
        'articulos': articulos,        
    }
    return render(request, 'articulos/listarArticulos.html',contexto)

# DETALLE ARTICULO
def detalleArticulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    comentarios = articulo.comentarios.all()


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







# SECCION CATEGORIA

# LISTAR CATEGORIAS
def listarCategorias(request):
    categorias = Categoria.objects.all()

    contexto = {
        'categorias': categorias,        
    }
    return render(request, 'categorias/listarCategorias.html',contexto)

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
    
    return render(request, 'categorias/addCategoria.html', {'form': form})


# SECCION DE COMENTARIOS

# AÑADIR COMENTARIOS
@login_required
def add_comment(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        usuario = request.user.username
        # creacion de comentario
        Comentario.objects.create(articulo_comentario=articulo, usuario_comentario=usuario, comentario=text)
    return redirect('articulos:detalleArticulos', pk=articulo_id)