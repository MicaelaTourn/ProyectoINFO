"""
URL configuration for blog_cocina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def consola_admin(request):
    return redirect('/admin/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('acerca de/', views.acerca_de, name='acerca_de'),
    path('usuarios/', include('apps.usuarios.urls')),
    path('articulos/',include('apps.articulos.urls')),
    path('contacto/', include('apps.contacto.urls')),
    path('administrador/', consola_admin, name='administrador'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
