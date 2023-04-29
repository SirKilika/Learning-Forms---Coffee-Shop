from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def coffee(request):
    template = loader.get_template('coffee.html')
    context = {}
    return HttpResponse(template.render(context, request))
