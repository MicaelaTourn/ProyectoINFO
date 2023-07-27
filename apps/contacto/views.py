from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        
        if form.is_valid():
            # Process the form data
            nuevoContacto = form.save(commit=False)
            nombreRemitente = request.POST.get('nombre')
            apellidoRemitente = request.POST.get('apellido')
            mensajeEnviado = request.POST.get('mensaje')
            emailRemitente = request.POST.get('email')
            
            data = {
                'nombre': nombreRemitente,
                'apellido': apellidoRemitente,
                'email': emailRemitente,
                'mensaje': mensajeEnviado
            }
            message = '''
            NuevoMensaje: {}


            From: {}
            '''.format(data['mensaje'],data['email'])
            nuevoContacto.save()
            send_mail(f'Contacto desde la web: {nombreRemitente} {apellidoRemitente}', message, '',['blogcocinagrupo4@gmail.com'])
            messages.add_message(request,level=messages.SUCCESS, message='Formulario enviado!')
            return redirect('home')
        else:
            messages.add_message(request,level=messages.ERROR, message='Todos los campos deben ser completados!')
    else:
        form = ContactForm()
    return render(request, 'contacto.html', {'form': form})


def success(request):
   return HttpResponse('Enviado!')