from django.shortcuts import render
from .models import Regione, Turista
from .form import ContactoForm, RegionForm
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
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
    return render(request, 'turismo/Contacto.html', data)

def agregar_region(request):
    data = {
        'form': RegionForm()
    }
    if request.method == 'POST':
        formulario = RegionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "region agregada"
        else:
            data["form"] = formulario
    return render(request, 'turismo/region/agregar.html', data)