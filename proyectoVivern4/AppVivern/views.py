from django.shortcuts import render
from .models import FamiliarMayor
from django.http import HttpResponse


# Create your views here.
def familiar(request):

    familiar1=FamiliarMayor(nombre="Virginia", apellido="Escayola", edad=47, nacimiento=6/28/1975, email="virescayola@gmail.com")
    familiar1.save()
    cadena_texto=f"familiar guadrado: Nombre: {familiar1.nombre}, Apellido:{familiar1.apellido},Edad:{familiar1.edad}, Nacimiento:{familiar1.nacimiento}, Email:{familiar1.email}"
    return HttpResponse(cadena_texto)