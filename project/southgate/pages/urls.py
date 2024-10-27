from django.urls import path
from pages.views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('aboutus/', about, name='aboutus'),
    path('servicedetails/<slug:service_title>/<str:servicefaq_service>', servicedetails, name='servicedetails'),
    path('vacancies/<slug:country_name>/<str:countryfaq_country>', jobvacancies, name='vacancies'),
]

