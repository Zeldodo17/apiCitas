from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, authentication
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

from Citas.models import Citas
from .serializares import DateSerializer

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class crudDate(APIView):
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
class UpdateDate(APIView):
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
            print(serializer.data)
            print(request.data)
            print('-----------------------------')
            print(date.Sintomas)
            return Response({'message': 'Error al actualizar cita', 'serializer':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)