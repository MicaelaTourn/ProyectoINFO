from django.shortcuts import render, redirect
from .models import Contacto
from .forms import ContactoForm


def msj_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            contacto = form.save(commit=False)
            contacto.save()            
            return redirect('home')
    else:
        form = ContactoForm()
    return render(request,'contacto.html',{'form':form})
