from django.shortcuts import render
from django.http import HttpResponse
from Appfamily.models import Familia

# Create your views here.

def fam(request):
    familia1=Familia(nombre="Lyonel", apellido="Messi", telefono="123456", fecha_nacimiento="1985-01-05")
    familia2=Familia(nombre="Mario", apellido="Kempes", telefono="654321", fecha_nacimiento="1962-06-06")
    familia3=Familia(nombre="Ramiro", apellido="Rodriguez", telefono="987654", fecha_nacimiento="1983-12-06")
    familia1.save()
    familia2.save()
    familia3.save()
    texto=f"Miembros Familiares: "
    return HttpResponse (texto)