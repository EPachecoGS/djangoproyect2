import random

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, request, HttpResponseRedirect
from django.template import loader, RequestContext
from django.urls import reverse
from .models import Members
from .models import InputEcuacion
from .models import InputResultado
from django.core.files import File
from fractions import Fraction
# Create your views here.
def index(request):
    
    return render(request, "Bienvenida.html")

def inicio(request):

    return HttpResponseRedirect(reverse('index'))

def quizzes(request):
    plantilla = loader.get_template('quizzes.html')
    return HttpResponse(plantilla.render({}, request))

def archivos(request):
    plantilla = loader.get_template('archivos.html')
    return HttpResponse(plantilla.render({}, request))

    
def registro(request):
  plantilla = loader.get_template('registro.html')
  return HttpResponse(plantilla.render({}, request))
  

def ranking(request):
    mymembers = Members.objects.all().values()
    plantilla = loader.get_template('Segunda_pagina.html')
    context={
        'mymembers': mymembers,
    }
    return HttpResponse(plantilla.render(context, request)) 

def top(request):
    mymembers = Members.objects.all().values()
    plantilla = loader.get_template('Segunda_pagina.html')
    top10=[]
    top20=[]
    top30=[]
    x= 1
    for member in mymembers:
        nombre = member["firstname"]
        puntaje = member["puntaje"]
        usuario = [x,nombre,puntaje]
        if x <= 10:
            top10.append(usuario)
        elif x > 10 and x <= 20:
            top20.append(usuario)
        elif x <= 30 and x > 20:
            top30.append(usuario)
        
        x +=1

    context={
        'mymembers': mymembers,
        'top10': top10,
        'top20': top20,
        'top30': top30,
    }
    return HttpResponse(plantilla.render(context, request)) 


def tablas(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('tablas.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('registro.html')
    return HttpResponse(template.render({}, request))

def formulario(request):
    mymembers = Members.objects.all().values() 
    name = request.POST['Usuario']
    last = request.POST['Contraseña']
    personas = []
    for member in mymembers:
        id = member["id"]
        nombre= member['firstname']
        contrasena = member['lastname']          
        member = [id,nombre, contrasena]
        personas.append(member)

    for persona in personas:
        id = persona[0]
        nombre = persona[1]
        contrasena= persona[2]
        if name == nombre and contrasena == last:
            mymembers = Members.objects.all().values()
            plantilla = loader.get_template('Segunda_pagina.html')
            context={
                'mymembers': mymembers,
            }
            return HttpResponse(plantilla.render(context, request)) 
    return HttpResponseRedirect(reverse('index'))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname = x, lastname = y, puntaje= 0)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('tablas'))

def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('tablas'))

def home(request):

    temporal = open('Proyecto2/Proyecto2/temporal.txt', 'r')
    guardado = temporal.read()
    separado = guardado.split(",")
    temporal.close

    if request.method == "POST" and guardado != "":

        multiplicador = separado[0]
        suma = separado[1]
        solucion = separado[2]
        multiplicadorRespuesta = separado[3]
        sumaRespuesta = separado[4]
        solucionRespuesta = separado[5]
        estado = separado[6]
        resuelto = separado [7]

        if int(suma) == 0:
            
            if estado == "no":

                multiplicadorRespuesta = Fraction(int(multiplicador), int(request.POST["numero"]))

                solucionRespuesta = Fraction(int(solucion), int(request.POST["numero"]))

                sumaRespuesta = suma
                estado = "si"

            else:

                if request.POST["suma"] == sumaRespuesta:

                    if request.POST["solucion"] == solucionRespuesta:

                        if request.POST["multiplicador"] == multiplicadorRespuesta:

                            multiplicador = multiplicadorRespuesta
                            solucion = solucionRespuesta
                            estado = "no"

        else:
            
            if estado == "no":

                sumaRespuesta = int(int(suma) + int(request.POST["numero"]))
                solucionRespuesta = int(int(solucion) + int(request.POST["numero"]))
                multiplicadorRespuesta = multiplicador
                estado = "si"

            else:

                if request.POST["suma"] == sumaRespuesta:

                    if request.POST["solucion"] == solucionRespuesta:

                        if request.POST["multiplicador"] == multiplicadorRespuesta:

                            suma = sumaRespuesta
                            solucion = solucionRespuesta
                            estado = "no"

        ecuacion = str(multiplicador) + "x" + " + " + str(suma) + " = " + str(solucion)

    else:

        suma = 0
        solucion = 0
        multiplicador = 0
        multiplicadorRespuesta = 0
        sumaRespuesta = 0
        solucionRespuesta = 0
        estado = "no"
        resuelto = "no"

        while suma == 0:

            suma = random.randint(-20, 20)

        while solucion == 0:

            solucion = random.randint(-20, 20)

        while multiplicador == 0:

            multiplicador = (solucion - suma) * random.randint(-5, 5)

        ecuacion = str(multiplicador) + "x" + " + " + str(suma) + " = " + str(solucion)
        
    temporal = open('Proyecto2/Proyecto2/temporal.txt', 'w')
    temporal.write(str(multiplicador) + "," + str(suma) + "," + str(solucion) + "," + str(multiplicadorRespuesta) + "," + str(sumaRespuesta) + "," + str(solucionRespuesta) + "," + str(estado) + "," + str(resuelto))
    temporal.close

    if int(multiplicador) <= 1 and int(multiplicador) >= 0:

        temporal = open('Proyecto2/Proyecto2/temporal.txt', 'w')
        temporal.truncate(0)
        temporal.close 
        resuelto = "si"

    if int(multiplicador) >= -1 and int(multiplicador) <= 0:

        temporal = open('Proyecto2/Proyecto2/temporal.txt', 'w')
        temporal.truncate(0)
        temporal.close
        resuelto = "si"

    respuesta = InputEcuacion()
    resultados = InputResultado()

    return render(request, "home.html/", {"respuesta":respuesta, "resultados":resultados, "ecuacion": ecuacion, "estado": estado, "resuelto": resuelto})



