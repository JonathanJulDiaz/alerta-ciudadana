from django.shortcuts import render, redirect
from .models import Reporte, PreguntaFrecuente

import requests

def landing_page(request):
    preguntas = PreguntaFrecuente.objects.all()
    return render(request, 'index.html', {'preguntas': preguntas})

def about_us(request):
    return render(request, 'about_us.html')

def chatbot(request):
    return render(request, 'chatbot.html')

def crear_reporte(request):
    return render(request, 'formulario.html')

def dashboard(request):
    reportes = Reporte.objects.order_by('-fecha')
    return render(request, 'dashboard.html', {'reportes': reportes})

def agradecimiento(request):
    return render(request, 'gracias.html')