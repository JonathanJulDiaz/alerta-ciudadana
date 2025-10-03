from django.urls import path
from reportes import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('about_us/', views.about_us, name='about_us'),
    path('reportar/', views.crear_reporte),
    path('gracias/', views.agradecimiento, name='gracias'),
    path('dashboard/', views.dashboard),
]