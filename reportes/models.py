from django.db import models

class Reporte(models.Model):
    CATEGORIAS = [
        ('robo', 'Robo'),
        ('violencia', 'Violencia'),
        ('acoso', 'Acoso'),
        ('ambiental', 'Riesgo Ambiental'),
        ('otro', 'Otro'),
    ]
    
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    descripcion = models.TextField(blank=False, null=False)
    ubicacion = models.CharField(max_length=255) # Pronto se mejorará
    fecha = models.DateTimeField(auto_now_add=True)
    anonimo = models.BooleanField(default=True)
    nombre_contacto = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.categoria} en {self.ubicacion} el {self.fecha}"
