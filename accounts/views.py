from rest_framework.response import Response
from . models import *
from . serializers import *
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            print("Error found")
        except Exception as e:
            print(e)
            return Response({"status":0,"message":str(e)},
                            status=status.HTTP_400_BAD_REQUEST)