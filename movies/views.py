from django.shortcuts import render
from django.http import HttpResponse    
from django.template import loader
from .models import Name

# Create your views here.

def index(request):
    template = loader.get_template("mainsite.html")
    return HttpResponse(template.render())

def bienvenida(request):
    mymovies = Name.objects.all().values()
    template = loader.get_template("bienvenida.html")
    context = {
        'mymovies': mymovies
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymovies = Name.objects.get(id=id)
    template = loader.get_template("detail.html")
    context = {
        'mymovies':mymovies
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template("contact.html")
    return HttpResponse(template.render())

