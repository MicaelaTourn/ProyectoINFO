from django.urls import path
from . import views

app_name = 'contacto'

urlpatterns = [
    path('contacto/', views.msj_contacto, name='msj_contacto'),
]
