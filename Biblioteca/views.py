from django.shortcuts import render
from .models import *

def index(request):
    navItem = NavItem.objects.all
    context = {
        "NavItem": navItem,
    }
    return render(request, 'Biblioteca/index.html', context)

def autores(request):
    navItem = NavItem.objects.all
    q = request.GET.get('q', '')  
    if q:
        autores = Autor.objects.filter(nombre__icontains=q)  
    else:
        autores = Autor.objects.all()  
    
    context = {
        'autores': autores,
        "NavItem": navItem,
    }
    return render(request, 'Biblioteca/autores.html', context)

def categorias(request):
    navItem = NavItem.objects.all
    query = request.GET.get('q', '')
    if query:
        categorias = Categoria.objects.filter(nombre__icontains=query)
    else:
        categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
        "NavItem": navItem,
    }
    return render(request, 'Biblioteca/categorias.html', context)

def libros(request):
    navItem = NavItem.objects.all
    query = request.GET.get('q')  
    if query:
        libros = Libro.objects.filter(titulo__icontains=query) 
    else:
        libros = Libro.objects.all() 
    
    context = {
        'libros': libros,
        "NavItem": navItem,
    }
    return render(request, 'Biblioteca/libros.html', context)