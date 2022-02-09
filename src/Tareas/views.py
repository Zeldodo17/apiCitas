from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, authentication
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from Citas.models import Citas
from .models import Tareas
from .serializer import (
        TaskSerializer, 
        TaskUpdateSerializer, 
        TaskSerializer2
    )

# Listar todas las tareas
class listTasks(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, mascota):
        try:
            tasks = Tareas.objects.filter(citas=Citas.objects.get(Nombre_mascota=mascota))
            serializer = TaskSerializer2(tasks, many=True)
            return Response({'tasks': serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error al listar Citas'}, status=status.HTTP_400_BAD_REQUEST)

# Crear Tarea
@method_decorator(csrf_exempt, name='dispatch')
class createTask(APIView):

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):
        try:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Tarea creada exitosamente'}, status=status.HTTP_200_OK)
            return Response({'serializer':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message':'Error al crear la Tarea',}, status=status.HTTP_400_BAD_REQUEST)

# Actualizar tarea
class updateTask(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def put(self, request, pk):
        try:
            tarea = Tareas.objects.filter(id=pk).first()
            serializer = TaskUpdateSerializer(instance=tarea, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Tarea actualizada exitosamente'}, status=status.HTTP_200_OK)
            return Response({'message':'Tienes que llenar todos los campos', 'serializer':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message':'Error al actualizar Tarea',}, status=status.HTTP_400_BAD_REQUEST)

# Eliminar tarea
class deleteTask(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def delete(self, request, pk):
        try:
            tarea = Tareas.objects.filter(id=pk).first()
            if tarea:
                tarea.delete()
                return Response({'message':'Tarea eliminada exitosamente'}, status=status.HTTP_200_OK)
            return Response({'message':'No existe esa tarea'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message':'Error al eliminar la Tarea',}, status=status.HTTP_400_BAD_REQUEST)
