# mystic/views.py

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

def index(request):
    print(settings.TEMPLATES[0]['DIRS'])  # This should print the list of directories Django looks into for templates
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def cart(request):
    return render(request, 'cart.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    return render(request, 'shop.html')

def sproduct(request):
    return render(request, 'sproduct.html')
