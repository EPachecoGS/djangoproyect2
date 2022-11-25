from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, request, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

# Create your views here.
def index(request):
    
    return render(request, "Bienvenida.html")
    
def registro(request):

    return render(request, "registro.html")

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

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname = x, lastname = y)
    member.save()
    return HttpResponseRedirect(reverse('tablas'))

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




