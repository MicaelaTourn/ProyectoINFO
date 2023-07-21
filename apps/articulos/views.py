from django.shortcuts import render

# Create your views here.
def listarArticulos(request):
    return render(request,'listarArticulos.html')