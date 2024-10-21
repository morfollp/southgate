from django.shortcuts import render, redirect
from pages.models import *

def index(request):
    countries= Country.objects.all()
    services= Service.objects.all()
    context={
    'countries': countries,
    'services': services,

    }
    return render(request, 'index.html', context)
