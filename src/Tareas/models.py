from django.db import models

# Create your models here.
class Tareas(models.Model):
    titulo = models.CharField(max_length = 150, blank=False, null=False)
    estado = models.CharField(max_length = 150, default='Incompleto' ,blank=False, null=False)
    citas = models.ForeignKey("Citas.Citas", blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
    
    