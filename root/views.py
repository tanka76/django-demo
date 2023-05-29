from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HelloAPIView(APIView):
    def get(self, request):
        data = {
            'message': 'Hello, World!'
        }
        return Response(data, status=status.HTTP_200_OK)
    

class NewAPIView(APIView):
    def get(self, request):
        data = {
            'message': 'Microsoft Azure'
        }
        return Response(data, status=status.HTTP_200_OK)
