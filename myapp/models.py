from django.db import models
from django import forms

# Create your models here.
class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    puntaje = models.IntegerField()

class InputEcuacion(forms.Form):

     numero = forms.CharField(label="", max_length=10 )

class InputResultado(forms.Form):

     multiplicador = forms.CharField(label="", max_length=10 )
     suma = forms.CharField(label="", max_length=10 )
     solucion = forms.CharField(label="", max_length=10 )

