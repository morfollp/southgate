from django.shortcuts import render, redirect
from pages.models import *

def index(request):
    countries= Country.objects.all()
    services= Service.objects.all()
    testimonials= Testimonial.objects.all()
    context={
    'countries': countries,
    'services': services,
    'testimonials': testimonials,

    }
    return render(request, 'pages/index.html', context)

def about(request):
    context={}
    return render(request, 'pages/aboutus.html', context)
