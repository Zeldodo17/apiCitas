from rest_framework import serializers
from .models import Usuarios
from django.contrib.auth import password_validation, authenticate
from rest_framework.authtoken.models import Token

# SERIALIZADOR PARA LOS USUARIOS
class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    nombres = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    telefono = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()

    def create(self, validated_data):
        instance = Usuarios()
        instance.nombres = validated_data.get('nombres')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.telefono = validated_data.get('telefono')

        password = validated_data.get('password')
        password2 = validated_data.get('password2')
        if password != password2:
            raise serializers.ValidationError({'message':'Las contraseñas no coinciden'})
        instance.set_password(password)
        instance.save()
        return instance

    def validate_username(self, data):
        users = Usuarios.objects.filter(username = data)
        if len(users) != 0:
            raise serializers.ValidationError({'message':'Este nombre de usuario ya existe, ingrese uno nuevo'})
        return data

# SERIALIZADOR PARA ACTUALIZAR USUARIO
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'
    
    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

#SERIALIZADOR PARA EL LOGIN
class UserLoginSerializer(serializers.Serializer):

    # Campos que vamos a requerir
    username = serializers.CharField()
    password = serializers.CharField()

    # Primero validamos los datos
    def validate(self, data):
        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError({'message': 'Usuario y/o contraseña incorrectas'})
        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token
        self.context['user'] = user
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key