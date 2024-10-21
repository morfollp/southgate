from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from datetime import datetime    


# Create your models here.
class Faq(models.Model):
    title=models.CharField(max_length=50, unique= True)
    question= models.TextField(max_length= 500, blank= False)
    answer= models.TextField(max_length= 500, blank= False)

    class Meta:
        verbose_name= 'Faq' #editing name in admin panel
        verbose_name_plural= 'Faq(s)' #For printing Categories instead of Categorys
    def __str__(self):
        return self.title


class Country(models.Model):
    country_name=models.CharField(max_length=50, unique= True)
    slug= models.SlugField(max_length= 100, unique= True)
    capital= models.TextField(max_length= 255, blank= True)
    area= models.TextField(max_length= 255, blank= True)
    population= models.TextField(max_length= 255, blank= True)
    language= models.TextField(max_length= 255, blank= True)
    currency= models.TextField(max_length= 255, blank= True)
    government= models.TextField(max_length= 255, blank= True)
    regions= models.TextField(max_length= 255, blank= True)
    climate= models.TextField(max_length= 255, blank= True)
    major_industries= models.TextField(max_length= 255, blank= True)
    cultural_heritage= models.TextField(max_length= 255, blank= True)
    natural_features= models.TextField(max_length= 255, blank= True)
    membership= models.TextField(max_length= 255, blank= True)
    country_image= models.ImageField(upload_to= 'photos/countries', blank=True)
    faq=models.ForeignKey(Faq, on_delete=models.CASCADE, blank=True, null= True)

    class Meta:
        verbose_name= 'country' #editing name in admin panel
        verbose_name_plural= 'countries' #For printing Categories instead of Categorys

    def __str__(self):
        return self.country_name

class Service(models.Model):
    title=models.CharField(max_length=50, unique= True)
    description= models.TextField(max_length= 255, blank= False)
    service_image= models.ImageField(upload_to= 'photos/services', blank=False)
    title2=models.CharField(max_length=50, unique= True)
    description2= models.TextField(max_length= 255, blank= False)
    highlight1= models.TextField(max_length= 100, blank= False)
    highlight2= models.TextField(max_length= 100, blank= False)
    highlight3= models.TextField(max_length= 100, blank= False)
    highlight4= models.TextField(max_length= 100, blank= False)
    faq=models.ForeignKey(Faq, on_delete=models.CASCADE, blank=True, null= True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name= 'service' #editing name in admin panel
        verbose_name_plural= 'services' #For printing Categories instead of Categorys

    def __str__(self):
        return self.title

class Vacancy(models.Model):
    title=models.CharField(max_length=50, unique= False)
    description= models.TextField(max_length= 255, blank= False)
    age_limit=models.CharField(max_length=50, unique= True, blank= True)
    country= models.ForeignKey(Country, on_delete=models.CASCADE, null=False, blank= False)
    post_date= models.DateTimeField(default=datetime.now(), blank=True)
    last_date= models.DateTimeField(blank=True)
    is_active= models.BooleanField(default=True)

    class Meta:
        verbose_name= 'vacancy' #editing name in admin panel
        verbose_name_plural= 'vacancies' #For printing Categories instead of Categorys
    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.CharField(max_length=50, unique= False)
    subject= models.TextField(max_length= 255, blank= False)
    description= models.TextField(max_length= 255, blank= False)
    email= models.EmailField(max_length=254)
    phone= models.CharField(max_length=50, unique= False)

    class Meta:
        verbose_name= 'Contact' #editing name in admin panel
        verbose_name_plural= 'contacts' #For printing Categories instead of Categorys
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name=models.CharField(max_length=50, unique= False)
    title= models.CharField(max_length=50, unique= False)
    description= models.TextField(max_length= 255, blank= False)
    profile_image= models.ImageField(upload_to= 'photos/testimonials', blank=False)
    video_url= models.URLField(max_length=200)

    class Meta:
        verbose_name= 'testimonial' #editing name in admin panel
        verbose_name_plural= 'testimonials' #For printing Categories instead of Categorys
    def __str__(self):
        return self.name
