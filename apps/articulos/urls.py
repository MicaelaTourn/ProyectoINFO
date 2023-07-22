from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'articulos'

urlpatterns = [
    path('', views.listarArticulos, name='listarArticulos'),
    path('addArticulo/', views.AddArticulo, name='addarticulo'),
    path('addCategoria/', views.addCategoria, name='addcategoria'),
    path('categorias/', views.listarCategorias, name='listarCategorias'),
    path('detalleArticulos/<int:pk>', views.detalleArticulos, name='detalleArticulos'),
    path('comentario/add/<int:articulo_id>/', views.add_comentario, name='add_comentario'),
]
