from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, authentication
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

from Citas.models import Citas
from Usuarios.models import Usuarios
from .serializares import DateSerializer

# Create your views here.

class listDates(APIView):
    def get(self, request):
        try:
            dates = Citas.objects.all()
            serializer = DateSerializer(dates, many=True)
            return Response({'dates': serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error al listar Citas'}, status=status.HTTP_200_OK)

class listDate(APIView):
    def get(self, request, pk):
        try:
            date = Citas.objects.filter(id=pk).first()
            serializer = DateSerializer(date, many=False)
            return Response({'date': serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error al listar Citas'}, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='dispatch')
class createDate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):
        try:
            serializer = DateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': 'Cita creada exitosamente'}, status=status.HTTP_200_OK)
            return Response({'error': 'Tienes que llenar todos los campos', 'serializer':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:
            print(serializer.data)
            return Response({'message': 'Error al crear cita', 'serializer':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class updateDate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def put(self, request, pk):
        try:
            date = Citas.objects.filter(id=pk).first()
            serializer = DateSerializer(instance=date, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': 'Cita actualizada exitosamente'}, status=status.HTTP_200_OK)
            return Response({'error': 'Tienes que llenar todos los campos', 'serializer':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': 'Error al actualizar cita', 'serializer':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class deleteDate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def delete(self, request, pk):
        try:
            date = Citas.objects.filter(id=pk)
            if date:
                date.delete()
                return Response({'success': 'Cita eliminada exitosamente'}, status=status.HTTP_200_OK)
            return Response({'error': 'Tienes que llenar todos los campos'}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({'message': 'Error al actualizar cita'}, status=status.HTTP_400_BAD_REQUEST)
