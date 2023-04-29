from django.template import loader
from django.http import HttpResponse

def Home(request):
    template = loader.get_template("home.html")
    context = {}
    return HttpResponse(template.render(context,request))