from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Articulo, Categoria, Comentario
from .forms import ArticuloForm, CategoriaForm, ComentarioForm
from django.http import HttpResponseForbidden
from django.contrib import messages
""" --------------------------------------------------
                   ARTICULOS
-------------------------------------------------- """
# MUESTRA TODOS LOS ARTICULOS
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

# BUSCAR ARTICULO SELECCIONADO
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

# EDITAR ARTICULO
@login_required
def editArticulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)

    # Solo el autor puede editar la noticia
    if request.user.tipo_usuario == 'Miembro':
        return HttpResponseForbidden("No tenes permiso para editar esta noticia.")

    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artículo editado con éxito')
            return redirect('articulos:detalleArticulos', pk=pk)
    else:
        form = ArticuloForm(instance=articulo)

    contexto = {
        'form': form,
    }
    return render(request, 'articulos/edit_articulo.html', contexto)

# ELIMINAR ARTICULO         
@login_required
def delete_articulo(request, pk):
    articulo = get_object_or_404(Articulo, id=pk)
    articulo.delete()
    messages.success(request, 'Artículo Eliminado con éxito')
    return redirect('articulos:listarArticulos')

# CREAR ARTICULO
@login_required
def AddArticulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES) ##REQUEST FILE PARA LAS IMAGENES
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.usuario_articulo = request.user #autor de la noticia
            articulo.save()
            messages.success(request, 'Artículo agregado con éxito')
            return redirect('articulos:detalleArticulos', pk=articulo.pk)
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
            messages.success(request, 'Categoría agregada con éxito')
            return redirect('articulos:listarCategorias')
    else:
        form =CategoriaForm()
    
    return render(request, 'categorias/addCategoria.html', {'form': form})

# EDITAR CATEGORIA
@login_required
def edit_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    #mensaje de error si no sos el autor
    if request.user.tipo_usuario == 'publico':
        messages.error(request, 'No tienes permisos para editar este comentario.')        
        return redirect('articulos:listarCategorias')
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría editada con éxito')
            return redirect('articulos:listarCategorias')
    else:
        form = CategoriaForm(instance=categoria)

    contexto = {
        'form': form,        
    }
    return render(request, 'categorias/edit_categoria.html', contexto)

# BORRAR CATEGORIA
@login_required
def delete_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.user.is_staff or request.user.is_superuser:
        categoria.delete()        
        messages.success(request, 'Categoría eliminada con éxito')
    return redirect('articulos:listarCategorias')

""" --------------------------------------------------
                   COMENTARIOS
-------------------------------------------------- """

# AÑADIR COMENTARIOS
@login_required
def add_comentario(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)
    if request.method == 'POST':
        text = request.POST.get('comentario')
        usuario = request.user
        # creacion de comentario
        Comentario.objects.create(articulo_comentario=articulo, usuario_comentario=usuario, comentario=text)
    return redirect('articulos:detalleArticulos', pk=articulo_id)

# EDITAR COMENTARIOS
@login_required
def edit_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comentario editado con éxito')
            return redirect('articulos:detalleArticulos', pk=comentario.articulo_comentario.pk)
    else:
        form = ComentarioForm(instance=comentario)

    contexto = {
        'form': form,
        'comment': comentario,
    }
    return render(request, 'articulos/edit_comentario.html', contexto)

# BORRAR COMENTARIO
@login_required
def delete_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    if comentario.usuario_comentario_id == request.user.id or request.user.tipo_usuario == 'Colaborador' or request.user.is_staff:
        comentario.delete()
        messages.success(request, 'Comentario Eliminado con éxito')
    return redirect('articulos:detalleArticulos', pk=comentario.articulo_comentario.pk)