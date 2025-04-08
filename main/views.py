from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Consulta
from django.utils import timezone

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

@login_required(login_url='/estadisticas/')
def estadisticas(request):
    if not request.user.is_authenticated:
        return render(request, 'main/estadisticas.html')
    
    # Obtener estadísticas de consultas
    total_consultas = Consulta.objects.count()
    consultas_hoy = Consulta.objects.filter(fecha_consulta__date=timezone.now().date()).count()
    consultas_ultima_semana = Consulta.objects.filter(fecha_consulta__gte=timezone.now()-timezone.timedelta(days=7)).count()
    
    context = {
        'total_consultas': total_consultas,
        'consultas_hoy': consultas_hoy,
        'consultas_ultima_semana': consultas_ultima_semana,
    }
    
    return render(request, 'main/estadisticas.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('estadisticas')
        else:
            messages.error(request, 'Credenciales inválidas')
            return redirect('estadisticas')
    
    return redirect('estadisticas')
