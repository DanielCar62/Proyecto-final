from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio(request):
    
    return render(request, "Inicio.html")

def usuario(request):
    
    return render(request, "Usuarios.html")

def instrumento(request):
    
    return render(request, "Instrumento.html")

def amplificador(request):
    
    return render(request, "Amplificador.html")
