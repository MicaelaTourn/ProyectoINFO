from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'articulos'

urlpatterns = [
    path('', views.listarArticulos, name='listar'),
    path('addArticulo/', views.AddArticulo, name='addarticulo'),
]
