from django.urls import path
from pages.views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('aboutus/', about, name='aboutus'),
]

