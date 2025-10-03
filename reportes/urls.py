from django.urls import path
from reportes import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('reportar/', views.crear_reporte),
    path('gracias/', views.agradecimiento, name='gracias'),
    path('dashboard/', views.dashboard),
]