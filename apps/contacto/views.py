from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            nuevoContacto = form.save(commit=False)
            nuevoContacto.save()
            messages.add_message(request,level=messages.SUCCESS, message='Formulario enviado!')
            return redirect('home')
        else:
            messages.add_message(request,level=messages.ERROR, message='Todos los campos deben ser completados!')
    else:
        form = ContactForm()
    return render(request, 'contacto.html', {'form': form})


def success(request):
   return HttpResponse('Enviado!')