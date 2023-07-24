from django.urls import path
from . import views

app_name = 'formularioContacto'

urlpatterns = [
    path('', views.contact, name='contacto'),
]