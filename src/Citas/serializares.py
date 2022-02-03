from rest_framework import serializers
from .models import Citas
from Usuarios.models import Usuarios
"""
class DateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    Nombre_mascota = serializers.CharField()
    Propietario = serializers.CharField()
    Telefono = serializers.CharField()
    Fecha = serializers.DateField()
    Sintomas = serializers.CharField(max_length = 2000)

    def create(self, validated_data):
        return Citas.objects.create(**validated_data)
    
    def validate_nombre(self, data):
        date = Citas.objects.filter(Nombre_mascota=data)
        if len(date) != 0:
            raise serializers.ValidationError({'message':'Ya hay una cita para esa mascota, ingresa uno nuevo'})
        else:
            return data
"""

class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citas
        fields = '__all__'
    
    def create(self, request, validated_data):
        #queryset = Usuarios.objects.filter(nombres=validated_data['Propietario']).first()
        cita = Citas(
            Nombre_mascota=validated_data['Nombre_mascota'],
            Propietario=request.user.id,
            Telefono=validated_data['Telefono'],
            Fecha=validated_data['Fecha'],
            Sintomas=validated_data['Sintomas']
        )
        cita.save()
        return cita
