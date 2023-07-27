from django.urls import path
from . import views

app_name = 'contacto'

urlpatterns = [
    path('mensaje/', views.msj_contacto, name='mensaje'),
]
