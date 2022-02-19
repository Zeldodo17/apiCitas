from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, authentication
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

from Citas.models import Citas
from .serializares import DateSerializer, DateModelSerializer

# Create your views here.

class listDates(APIView):
    def get(self, request):
        try:
            dates = Citas.objects.all()
            if dates:
                serializer = DateSerializer(dates, many=True)
                return Response({'dates': serializer.data}, status=status.HTTP_200_OK)
            return Response({'error': 'No hay citas registradas'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Error al listar Citas'}, status=status.HTTP_200_OK)

class listDate(APIView):
    def get(self, request, pk):
        try:
            date = Citas.objects.filter(id=pk).first()
            if date:
                serializer = DateSerializer(date, many=False)
                return Response({'date': serializer.data}, status=status.HTTP_200_OK)
            return Response({'error': 'No hay citas registradas'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Error al listar Citas'}, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class createDate(APIView):
    # Aqui lo que se hace es decirle a la clase que va a estar protegida
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    # Aqui creamos el metodo post, el cual va a ser el metodo http por el cual funcionara la creación de Citas
    def post(self, request):
        try:
            # Le pasamos al serializer los datos que vienen del frontend
            serializer = DateSerializer(data=request.data)
            # Verificamos si el serializar es valido
            if serializer.is_valid():
                # Guardamos en la base de datos
                serializer.save()
                # Repondemos con un mensaje de exito
                return Response({'success': 'Cita creada exitosamente'}, status=status.HTTP_200_OK)
                # Repondemos con un mensaje de error
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:
            # Repondemos con un mensaje de error
            return Response({'error': 'Error al crear la cita'}, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class updateDate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def put(self, request, pk):
        try:
            date = Citas.objects.filter(id=pk).first()
            serializer = DateModelSerializer(instance=date, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': 'Cita actualizada exitosamente'}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': 'Error al actualizar cita'}, status=status.HTTP_400_BAD_REQUEST)

class deleteDate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def delete(self, request, pk):
        try:
            date = Citas.objects.filter(id=pk)
            if date:
                date.delete()
                return Response({'success': 'Cita eliminada exitosamente'}, status=status.HTTP_200_OK)
            return Response({'error': 'No existe ninguna cita con ese id'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': 'Error al actualizar cita'}, status=status.HTTP_400_BAD_REQUEST)
