from django.urls import path
from . import views
 
app_name = 'noticias'
 
urlpatterns = [
    path('', views.ListarNoticias, name= 'listar'),
    path('detalle/<int:pk>', views.DetalleNoticias, name= 'detalle'),
    path('addNoticia', views.AddNoticia, name='addnoticia'),

]
