from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ContactForm

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            nuevoContacto = form.save(commit=False)
            nuevoContacto.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contacto/contactoForm.html', {'form': form})


def success(request):
   return HttpResponse('Success!')