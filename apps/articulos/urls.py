from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'articulos'

urlpatterns = [
    # ARTICULOS URL
    path('', views.listarArticulos, name='listarArticulos'),
    path('addArticulo/', views.AddArticulo, name='addarticulo'),
    path('detalleArticulos/<int:pk>', views.detalleArticulos, name='detalleArticulos'),
    path('articulos/<int:pk>/edit/', views.editArticulo, name='editArticulo'),
    path('articulo/delete/<int:pk>/',views.delete_articulo , name='delete_articulo'),
    # CATEGORIAS URL
    path('addCategoria/', views.addCategoria, name='addcategoria'),
    path('categorias/', views.listarCategorias, name='listarCategorias'),
    path('categorias/edit/<int:categoria_id>/', views.edit_categoria, name='edit_categoria'),
    path('categorias/delete/<int:categoria_id>/', views.delete_categoria, name='delete_categoria'),
    # COMENTARIOS URL
    path('comentario/add/<int:articulo_id>/', views.add_comentario, name='add_comentario'),
    path('comentario/edit/<int:comentario_id>/', views.edit_comentario, name='edit_comentario'),
    path('comentario/delete/<int:comentario_id>/', views.delete_comentario, name='delete_comentario'),
]
