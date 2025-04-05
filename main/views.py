from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .models import Consulta

def home(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        
        # Verificar que tenemos todos los datos
        if nombre and email and mensaje:
            # Crear la consulta
            consulta = Consulta.objects.create(
                nombre=nombre,
                email=email,
                mensaje=mensaje
            )
            # Verificar que se creó correctamente
            if consulta:
                messages.success(request, '¡Mensaje enviado con éxito!')
            else:
                messages.error(request, 'Error al guardar el mensaje')
        else:
            messages.error(request, 'Por favor, completa todos los campos')
        
        return redirect('home')
    
    return render(request, 'main/index.html')

def articles(request):
    return render(request, 'main/articles.html')

def links(request):
    return render(request, 'main/links.html')

def contact(request):
    return render(request, 'main/contact.html')

def privacy(request):
    return render(request, 'main/privacy.html')
