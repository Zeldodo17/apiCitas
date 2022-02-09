from rest_framework import serializers
from .models import Tareas
from Citas.models import Citas

class TaskSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    titulo = serializers.CharField()
    estado = serializers.CharField(max_length=20, default='Incompleto')
    Nombre_mascota = serializers.CharField()

    def create(self, data):
        instance = Tareas()
        instance.titulo = data.get('titulo')
        instance.citas = Citas.objects.get(Nombre_mascota=data['Nombre_mascota'])
        instance.save()
        return instance

    def validate_Nombre_mascota(self, data):
        print(data)
        cita = Citas.objects.filter(Nombre_mascota=data)
        if len(cita) == 0:
            raise serializers.ValidationError({'message': 'No se encontro ninguna cita con esa mascota'})
        return data

    def validate_titulo(self, value):
        data = self.get_initial()
        cita = Citas.objects.get(Nombre_mascota=data.get("Nombre_mascota"))
        tarea = Tareas.objects.filter(titulo=value, citas=cita)
        if len(tarea) != 0:
            raise serializers.ValidationError({'message': 'Ya existe una tarea con ese titulo'})
        return value

class TaskUpdateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    titulo = serializers.CharField()
    estado = serializers.CharField(max_length=20, default='Incompleto')
    Nombre_mascota = serializers.CharField()

    def update(self, instance, data):
        instance.titulo = data.get('titulo', instance.titulo)
        instance.estado = data.get('estado', instance.estado)
        instance.citas = data.get(Citas.objects.get(Nombre_mascota=data['Nombre_mascota']), instance.citas)
        instance.save()
        return instance

class TaskSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__'