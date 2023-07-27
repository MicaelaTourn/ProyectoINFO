from django.shortcuts import render, redirect
from .models import Contacto
from .forms import ContactoForm

# formulario para recibir msj de la template de contacto
def msj_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            contacto = form.save(commit=False)
            contacto.save()            
            return redirect('home')
    else:
        form = ContactoForm()
    return render(request,'contacto/contacto.html',{'form':form})


def listarMensajes(request):
    mensajes = Contacto.objects.all()

    contexto = {
        'mensajes': mensajes,        
    }
    return render(request, 'contacto/listarMensajes.html',contexto)