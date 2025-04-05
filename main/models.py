from django.db import models

# Create your models here.

class Consulta(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_consulta = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['-fecha_consulta']  # Ordenar por fecha, más recientes primero

    def __str__(self):
        return f"Consulta de {self.nombre} - {self.fecha_consulta.strftime('%d/%m/%Y')}"
