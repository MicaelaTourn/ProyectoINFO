from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Articulo, Categoria, Comentario
from .forms import ArticuloForm, CategoriaForm, ComentarioForm

""" --------------------------------------------------
                   ARTICULOS
-------------------------------------------------- """
# Funcion para mostrar articulos
def listarArticulos(request):
    articulos = Articulo.objects.all()

    # FILTRAR POR CATEGORIA
    categoria = request.GET.get('categoria')
    if categoria:
        articulos =  articulos.filter(categoria_articulo=categoria)

    # FILTRAR POR ANTIGUEDAD
    antiguedad_asc = request.GET.get('antiguedad_asc')
    if antiguedad_asc:
        articulos= articulos.order_by('fecha_publicacion')

    # FILTRAR POR ANTIGUEDAD DESCENDENTE
    antiguedad_desc = request.GET.get('antiguedad_desc')
    if antiguedad_desc:
        articulos = articulos.order_by('-fecha_publicacion')
    
    # FILTRAR POR ORDEN ALFABETICO ASCENDENTE
    orden_asc = request.GET.get('orden_asc')
    if orden_asc:
        articulos = articulos.order_by('titulo')

    # FILTRAR POR ORDEN ALFABETICO DESCENDENTE
    orden_desc = request.GET.get('orden_desc')
    if orden_desc:
        articulos = articulos.order_by('-titulo')
    



    contexto = {
        'articulos': articulos,    
        'categorias': Categoria.objects.all(),    
    }
    return render(request, 'articulos/listarArticulos.html',contexto)

def detalleArticulos(request, pk):
    articulo = get_object_or_404 (Articulo, pk=pk)
    comentarios = articulo.comentarios.all()

    # COMENTARIO
    if request.method == 'POST' and 'add_comentario' in request.POST:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo_comentario= articulo
            comentario.usuario_comentario= request.user
            comentario.save()
            return redirect('articulos:detalleArticulos', pk=pk)
    else:
        form = ComentarioForm()
    contexto = {
        'articulo':articulo,
        'comentarios': comentarios,
        'form': form,
    }
    return render(request, 'articulos/detalleArticulos.html', contexto)

            
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


""" --------------------------------------------------
                   CATEGORIAS
-------------------------------------------------- """

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


""" --------------------------------------------------
                   COMENTARIOS
-------------------------------------------------- """

# AÑADIR COMENTARIOS
@login_required
def add_comentario(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)
    if request.method == 'POST':
        text = request.POST.get('comentario')
        usuario = request.user.username
        # creacion de comentario
        Comentario.objects.create(articulo_comentario=articulo, usuario_comentario=usuario, comentario=text)
    return redirect('articulos:detalleArticulos', pk=articulo_id)

