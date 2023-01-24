from django.shortcuts import render

from .models import Remera

# Create your views here.

def index(request):
    return render(request, 'shop/index.html')

def contacto(request):
    return render(request,'shop/contactos.html')



def mis_remeras(request):
    ctx = {'remeras': Remera.objects.all()}
    
    return render(request, 'shop/mis_remeras.html', ctx)