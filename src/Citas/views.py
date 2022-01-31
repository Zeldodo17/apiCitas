from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class Hola(APIView):
    def get(self, request):
        return Response({'usuario':request.user}, status=status.HTTP_200_OK)