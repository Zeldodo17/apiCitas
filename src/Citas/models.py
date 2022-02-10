from django.db import models


# Create your models here.
class Citas(models.Model):
    Nombre_mascota = models.CharField("Nombre de la Mascota", max_length=120, null=False, blank=False)
    Propietario = models.ForeignKey('Usuarios.Usuarios', null=False, blank=False, on_delete=models.CASCADE)
    Telefono = models.CharField("Número de telefono", max_length=10, null=False, blank=False)
    Fecha = models.DateField("Fecha de la cita", auto_now_add=False, auto_now=False, blank=False)
    Sintomas = models.CharField("Sintomas", max_length=2000, help_text="Aqui van los sintomas")

    def __str__(self):
        return f"{self.Nombre_mascota} - {self.Propietario}"
    
    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'