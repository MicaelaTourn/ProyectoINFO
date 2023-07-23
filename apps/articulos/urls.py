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
    # COMENTARIOS URL
    path('comentario/add/<int:articulo_id>/', views.add_comentario, name='add_comentario'),
    path('comentario/edit/<int:comentario_id>/', views.edit_comentario, name='edit_comentario'),
]
