from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuarios
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, UserModelSerializer
from rest_framework import status, permissions, authentication
from rest_framework.decorators import action
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import logout, login
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.utils.decorators import method_decorator

# Serializers
from .serializers import UserLoginSerializer, UserModelSerializer

# VISTA PARA LISTAR A TODOS LOS USUARIOS
class ListUsers(APIView):
    # AQUI PROTEGEMOS LA VISTA PARA QUE SOLO USUARIOS VALIDOS PUEDAN ACCEDER
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            # OBTENEMOS A TODOS LOS USUARIOS
            users = Usuarios.objects.all()
            serializer = UserModelSerializer(users, many=True)
            return Response({'users': serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'message':'Error al listar usuarios'}, status=status.HTTP_400_BAD_REQUEST)

# VISTA PARA CREAR USUARIOS
@method_decorator(csrf_exempt, name='dispatch')
class CreateUser(APIView):
    # AQUI LE DECIMOS A LA VISTA QUE PERMITA TODO
    permissions_classes = [permissions.AllowAny, ]

    def post(self, request):
        try:
            # AQUI LE PASAMOS LOS DATOS QUE VIENEN DEL FRONTEND AL SERIALIZADOR
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Usuario creado exitosamente'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message':'Tienes que llenar todos los campos'}, status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message':'Error al crear usuario'}, status = status.HTTP_400_BAD_REQUEST)

# VISTA PARA EL LOGIN DE USUARIOS
@method_decorator(csrf_exempt, name='dispatch')
class LoginUser(APIView):
    # AQUI LE DECIMOS A LA VISTA QUE PERMITA TODO
    permission_classes = (permissions.AllowAny,) 
    # authentication_classes = (authentication.TokenAuthentication,)

    queryset = Usuarios.objects.filter(activo=True)
    serializer_class = UserModelSerializer

    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post
    @action(detail=False, methods=['POST'])
    def post(self, request):
        try:
            serializer = UserLoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user, token = serializer.save()
            login(request, user)
            data = {
                'user': UserModelSerializer(user).data,
                'access_token': token
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response({'message':'Error al iniciar sesion'}, status=status.HTTP_400_BAD_REQUEST)

# VISTA PARA CERRAR SESION
class LogoutUser(APIView):
    # AQUI PROTEGEMOS LA VISTA PARA QUE SOLO USUARIOS VALIDOS PUEDAN ACCEDER
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        try:
            # Aqui eliminamos el token que se genero para el usuario
            request.user.auth_token.delete()
            logout(request)
            return Response({'success':'Has cerrado sesión correctamente'}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Algo fue mal durante el logout'}, status=status.HTTP_400_BAD_REQUEST)

# VISTA PARA ACTUALIZAR USUARIOS
@method_decorator(csrf_exempt, name='dispatch')
class UpdateUser(APIView):
    # AQUI PROTEGEMOS LA VISTA PARA QUE SOLO USUARIOS VALIDOS PUEDAN ACCEDER
    authentication_classes = [authentication.TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]
    def put(self, request, pk):
        try:
            # aqui obtenemos al usuario segun su id
            user = Usuarios.objects.filter(id=pk).first()
            # aqui pasamos una instancia del usuario y los datos nuevos que vienen del frontend
            serializer = UserModelSerializer(instance=user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'El usuario se ha actualizado exitosamente'}, status=status.HTTP_200_OK)
            return Response({'message':'Debes llenar todos los campos'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message':'Error al actualizar al usuario'}, status=status.HTTP_400_BAD_REQUEST)

# VISTA PARA ELIMINAR USUARIOS
@method_decorator(csrf_exempt, name='dispatch')
class DeleteUser(APIView):
    # AQUI PROTEGEMOS LA VISTA PARA QUE SOLO USUARIOS VALIDOS PUEDAN ACCEDER
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, pk):
        try:
            # aqui obtenemos al usuario segun su id
            user = Usuarios.objects.filter(id=pk).first()
            if user:
                user.delete()
                return Response({'message':'Usuario eliminado exitosamente'}, status=status.HTTP_200_OK)
            return Response({'message':'No existe ese usuario'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message':'Error al eliminar usuario'}, status=status.HTTP_400_BAD_REQUEST)
        
# VISTA PARA OBTENER EL CSRF TOKEN
@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({'succes': 'CSRF cookie set'})
