import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer


logger=logging.getLogger(__name__)

class HelloAPIView(APIView):
    logger.info("This is HelloAPIView Start")
    def get(self, request):
        data = {
            'message': 'Hello, World!'
        }
        logger.info("This is HelloAPIView End")

        return Response(data, status=status.HTTP_200_OK)
    

class NewAPIView(APIView):
    def get(self, request):

        logger.info("This is NewAPIView Start")

        data = {
            'message': 'Microsoft Azure'
        }
        logger.info("This is NewAPIView End")

        return Response(data, status=status.HTTP_200_OK)


#list of users
# views.py


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
