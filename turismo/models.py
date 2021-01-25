from django.db import models


class Regione(models.Model): #creacion de la tabla region
    id_region = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)

    def __str__(self): #valor principal que muestra en la tabla region
        return self.nombre

    # Create your models here.

class Turista(models.Model):#creacion de tabla turista
    Run = models.TextField()
    Nombre = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=10)
    Email = models.EmailField()
    

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre