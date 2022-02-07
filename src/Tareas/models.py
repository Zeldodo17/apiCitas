from django.db import models

# Create your models here.
class Tareas(models.Model):
    nombre = models.CharField(max_length = 150, blank=False, null=False)
    estado = models.CharField(max_length = 150, default='Pendiente' ,blank=False, null=False)
    citas = models.ForeignKey("Citas.Citas", blank=False, null=False, on_delete=models.CASCADE)
    
    