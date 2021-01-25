from django.shortcuts import render
from .models import Regione, Turista
from .form import ContactoForm
# Create your views here.
def index(request):#muestra pagina inicial
    
    return render(request, 'turismo/index.html')

def Registro(request):#muestra pagina inicial
    return render(request, 'turismo/Registro.html', {})

def Lugar1(request):#muestra pagina inicial
    return render(request, 'turismo/Lugar1.html', {})

def IniciarSesion(request):#muestra pagina inicial
    return render(request, 'turismo/IniciarSesion.html', {})

def Contacto(request):
    data = {
        'form': ContactoForm()
    }
    return render(request, 'turismo/Contacto.html', data)