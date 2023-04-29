from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

def member(request):
    return HttpResponse("Hello World!")

