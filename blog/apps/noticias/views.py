from django.shortcuts import render
from .models import Noticia, Categoria
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import NoticiaForm
from django.contrib.auth.decorators import login_required



# Create your views here.

def ListarNoticias(request):
    contexto = {} #diccionario
    id_categoria = request.GET.get("id", None)


    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia = id_categoria)
    else:
        n = Noticia.objects.all() #SELECT * FROM Noticias / lista objetos


    contexto['noticias'] = n


    cat = Categoria.objects.all().order_by('nombre') #ordena por nombre
    contexto['categorias'] = cat


    return render(request, 'noticias/listar.html', contexto)



def DetalleNoticias(request, pk):
    contexto = {}
 
    n = Noticia.objects.get(pk = pk) #retorna un objeto
    contexto['noticia'] = n
 
    return render(request, 'noticias/detalle.html', contexto)

def AddNoticia(request):
    form = NoticiaForm(request.POST or None, request.FILES) ##REQUEST FILE PARA LAS IMAGENES


    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(reverse('home'))
    return render(request, 'noticias/addNoticia.html', {'form': form})