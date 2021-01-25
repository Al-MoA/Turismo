from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Registro', views.Registro, name='Registro'),
    path('Lugar1', views.Lugar1, name='Lugar1'),
    path('inicarsesion', views.IniciarSesion, name='IniciarSesion'),
    path('Contacto', views.Contacto, name='Contacto'),
]