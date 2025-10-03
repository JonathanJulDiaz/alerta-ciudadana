from django.shortcuts import render, redirect
from .models import Reporte

import requests

def landing_page(request):
    return render(request, 'index.html')

def crear_reporte(request):
    
    if request.method == 'POST':
        categoria = request.POST['categoria']
        descripcion = request.POST['descripcion']
        ubicacion = request.POST['ubicacion']
        anonimo = request.POST.get('anonimo') == 'on'
        nombre = request.POST.get('nombre_contacto') if not anonimo else ''
        email = request.POST.get('email') if not anonimo else ''

        reporte = Reporte.objects.create(
            categoria=categoria,
            descripcion=descripcion,
            ubicacion=ubicacion,
            anonimo=anonimo,
            nombre_contacto=nombre,
            email=email
        )

        # Llamar al webhook de n8n
        data = {
            'categoria': reporte.categoria,
            'descripcion': reporte.descripcion,
            'ubicacion': reporte.ubicacion,
            'fecha': str(reporte.fecha),
        }
        try:
            requests.post('https://yamidt.app.n8n.cloud/webhook-test/d8bcb5eb-b711-4c03-8d30-45c8c87e50cb',
                          json=data)
        except:
            print("Error al llamar al webhook de n8n")
            pass

        return redirect('gracias')
    return render(request, 'formulario.html')

def dashboard(request):
    reportes = Reporte.objects.order_by('-fecha')
    return render(request, 'dashboard.html', {'reportes': reportes})

def agradecimiento(request):
    return render(request, 'gracias.html')