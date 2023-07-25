from django.urls import path
from . import views

app_name = 'contacto'

urlpatterns = [
    path('formulario-contacto', views.contact, name='formContacto'),
]