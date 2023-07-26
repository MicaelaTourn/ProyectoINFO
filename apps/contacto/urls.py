from django.urls import path
from . import views
from blog_cocina.views import contacto

app_name = 'contacto'

urlpatterns = [
    path('', views.contact, name='contacto'),
]