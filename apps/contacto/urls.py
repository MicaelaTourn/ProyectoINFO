from django.urls import path
from . import views

app_name = 'contacto'

urlpatterns = [
    path('mensajes/', views.listarMensajes, name='mensajes'),
    path('', views.msj_contacto, name='contacto'),
]
