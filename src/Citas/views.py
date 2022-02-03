from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, authentication
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from .serializares import DateSerializer

# Create your views here.
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
            else:
                print(serializer.data)
                return Response({'error': 'Tienes que llenar todos los campos', 'serializer':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': 'Error al crear cita', 'serializer':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)