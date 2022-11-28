from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, request, HttpResponseRedirect
from django.template import loader, RequestContext
from django.urls import reverse
from .models import Members

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
  plantilla = loader.get_template('Segunda_pagina.html')
  return HttpResponse(plantilla.render({}, request))


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
'''
def formulario(request):
    mymember = Members.objects.all().values() 
    name = request.POST['Usuario']
    last = request.POST['Contraseña']
    for x in mymember:
        a = x[2]
        b = x[1]
        if (name == a) and (last == b):
            plantilla = loader.get_template('Segunda_pagina.html')
            return HttpResponse(plantilla.render({}, request))
        else:

            return HttpResponseRedirect(reverse('index'))
'''
def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname = x, lastname = y)
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




