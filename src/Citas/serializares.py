from rest_framework import serializers
from .models import Citas
from Usuarios.models import Usuarios
from Usuarios.serializers import UserModelSerializer

class DateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    Nombre_mascota = serializers.CharField()
    Propietario = serializers.CharField()
    Telefono = serializers.CharField()
    Fecha = serializers.DateField()
    Sintomas = serializers.CharField(max_length = 2000)

    def create(self, data):
        instance = Citas()
        instance.Nombre_mascota = data.get('Nombre_mascota')
        instance.Propietario = Usuarios.objects.get(nombres=data['Propietario'])
        instance.Telefono = data.get('Telefono')
        instance.Fecha = data.get('Fecha')
        instance.Sintomas = data.get('Sintomas')
        instance.save()
        return instance
    
    def update(self, instance, data):
        instance.Nombre_mascota = data.get('Nombre_mascota', instance.Nombre_mascota)
        instance.Propietario = data.get(Usuarios.objects.get(nombres=data['Propietario']), instance.Propietario)
        instance.Telefono = data.get('Telefono', instance.Telefono)
        instance.Fecha = data.get('Fecha', instance.Fecha)
        instance.Sintomas = data.get('Sintomas', instance.Sintomas)
        instance.save()
        return instance
    
    
    
    def validate_nombre(self, data):
        date = Citas.objects.filter(Nombre_mascota=data)
        if len(date) != 0:
            raise serializers.ValidationError({'message':'Ya hay una cita para esa mascota, ingresa uno nuevo'})
        else:
            return data


"""
class UpdateDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citas
        fields = '__all__'
    
    def update(self, instance, data):
        date = super().update(instance, data)
        date.Propietario = Usuarios.objects.get(nombres=data['Propietario'])
        date.save()
        return date
"""

