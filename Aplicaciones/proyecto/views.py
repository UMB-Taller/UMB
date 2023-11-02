from django.shortcuts import render
from .models import Proyecto

# Create your views here.

def proyecto(request):
    mis_proyectos = Proyecto.objects.all()
    return render(request,"proyectos.html",{"proyecto":mis_proyectos})