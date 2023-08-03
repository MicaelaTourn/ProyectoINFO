from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto
from .forms import ContactoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# formulario para recibir msj de la template de contacto
def msj_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            contacto = form.save(commit=False)
            contacto.save()        
            messages.success(request, 'Mensaje enviado con éxito')    
            return redirect('home')
    else:
        form = ContactoForm()
    return render(request,'contacto/contacto.html',{'form':form})

# LISTAR MENSAJES DE LOS CONTACTOS
def listarMensajes(request):
    mensajes = Contacto.objects.all()

    contexto = {
        'mensajes': mensajes,        
    }
    return render(request, 'contacto/listarMensajes.html',contexto)

# BORRAR MENSAJE DE LOS CONTACTOS
@login_required
def delete_mensaje(request, mensaje_id):
    mensaje = get_object_or_404(Contacto, id=mensaje_id)
    if request.user.is_staff or request.user.is_superuser:
        mensaje.delete()        
        messages.success(request, 'Mensaje Eliminado con éxito')
    return redirect('contacto:mensajes')