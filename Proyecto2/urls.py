"""Proyecto2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index, name="index"),
    path("formulario/", formulario, name="formulario"),
    path("registro/", registro, name="registro"),
    path("registro/addrecord/", addrecord, name= "addrecord"),
    path("Segunda_pagina/", ranking, name="ranking"),
    path("Segunda_pagina/top/", top, name ="top"),
    path("Segunda_pagina/quizzes/", home, name="quizzes"),
    path("Segunda_pagina/quizzes/home/", home, name="home"),
    path("Segunda_pagina/quizzes/home/Bienvenida/", inicio, name="inicio"),
    path("Segunda_pagina/quizzes/Bienvenida/", inicio, name="inicio"),
    path("Segunda_pagina/archivos/", archivos, name="archivos"),
    path("Segunda_pagina/tablas/", tablas, name="tablas"),
    path("Segunda_pagina/archivos/Bienvenida/", inicio, name="inicio"),
]
