from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .forms import UserForm, UserDetailsForm
from django.contrib.auth import login, get_user_model
from django.forms import inlineformset_factory
from .models import Coffee
from .formset import BaseOrderFormSet


def coffee(request):
    template = loader.get_template('coffee.html')
    context = {}
    return HttpResponse(template.render(context, request))


def thanks(request):
    template = loader.get_template('thanks.html')
    context = {}
    return HttpResponse(template.render(context, request))


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect("/order/")
    else:
        form = UserForm(initial={"email": "@gmail.com"})

    return render(request, "signup.html", {"form": form})


def details(request):
    if request.method == "POST":
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thanks/")
    else:
        form = UserDetailsForm(initial={"username": request.user.username, "email": request.user.email})

    return render(request, "signup.html", {"form": form})


def placeorder(request):
    #OrderFormSet = modelformset_factory(Coffee, fields=["name", "size", "quantity"], max_num=10, extra=3,
    #                                   validate_max=True, can_delete=True)
    OrderFormSet = inlineformset_factory(get_user_model(), Coffee, formset=BaseOrderFormSet, fields=["name", "size", "quantity"], max_num=5,
                                         extra=2, validate_max=True, can_delete=True)
    user = get_user_model().objects.get(username=request.user.username)
    if request.method == "POST":
        order_formset = OrderFormSet(request.POST, instance=user)
        if order_formset.is_valid():
            order_formset.save()
            return redirect("coffee")
    else:
        order_formset = OrderFormSet(
                                     queryset=Coffee.objects.none(),
                                     instance=user)
    return render(request, "order.html", {"formset": order_formset})
