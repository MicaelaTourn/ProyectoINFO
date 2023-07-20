from django.urls import path
from . import views
 
app_name = 'noticias'
 
urlpatterns = [
    path('', views.ListarNoticias, name= 'listar'),
    path('detalle/<int:pk>', views.DetalleNoticias, name= 'detalle'),
    path('addNoticia', views.AddNoticia, name='addnoticia'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('comment/add/<int:noticia_id>/', views.add_comment, name='add_comment'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('noticias/<int:pk>/edit/', views.EditNoticia, name='edit_noticia'),
]
