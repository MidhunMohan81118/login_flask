#for function based view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializers import *

from rest_framework import generics,mixins

#for class based view
from rest_framework.views import APIView

# For Token authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

#JWT Authentication
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
@api_view()
def home(request):
    return Response({
        "status":200, "message":"Hello from Django Rest Framework"
    })


########------------function based view

# @api_view(['GET'])
# def studentdata(request):
#     student = Student.objects.all()
#     serializer = StudentSerializer(student, many=True)
#     return Response({
#         "status":1, "message":"Student Data", 
#         "data":serializer.data
#     },status=status.HTTP_200_OK)


# @api_view(['POST'])
# def post_student(request):
#     data=request.data
#     serializer =StudentSerializer(data=request.data)
#     if request.data["age"]<18:
#         return Response({"status":0,"message":"Age should be greater than 18"},
#                         status=status.HTTP_400_BAD_REQUEST)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"status":1,"message":"Student Data Added Successfully"},
#                         status=status.HTTP_201_CREATED)
#     else:
#         return Response({"status":0,"message":serializer.errors},
#                         status=status.HTTP_400_BAD_REQUEST)
    
    
# @api_view(['PUT','PATCH'])
# def update_student(request,pk):
#     try:
#         student = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(student,data=request.data, partial=True) 
#         if not serializer.is_valid():
#             return Response({"status":0,"message":serializer.errors},
#                             status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response({"status":1,"message":"Student Data Updated Successfully"},
#                         status=status.HTTP_200_OK)
#     except Student.DoesNotExist:
#         return Response({"status":0,"message":"Student Not Found"},
#                         status=status.HTTP_404_NOT_FOUND)
    
# @api_view(['DELETE'])
# def delete_student(request,id):
#     try:
#         student = Student.objects.get(pk=id)
#         student.delete()
#         return Response({"status":1,"message":"Student Data Deleted Successfully"},
#                         status=status.HTTP_200_OK)
#     except Student.DoesNotExist:
#         return Response({"status":0,"message":"Student Not Found"},
#                         status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_book(request):
    book = Book.objects.all()
    serializer = BookSerializer(book,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)



######################------------------------Class based view
class StudentAPI(APIView):

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    authentication_classes = [JWTAuthentication]
    parser_classes = [IsAuthenticated]

    def get(self,request):
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        data=request.data
        serializer = StudentSerializer(data=data)
        if not serializer.is_valid():
            return Response({"status":0,"message":serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"status":1,"message":"Student Data Added Successfully",
                         "data":serializer.data},status=status.HTTP_200_OK)

    def put(self,request,id):
        try:
            student=Student.objects.get(id=id)
            serializer = StudentSerializer(student,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":1,"message":"Student Data Updated Successfully",
                                 "data":serializer.data},status=status.HTTP_200_OK)
            return Response({"status":0,"message":serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({"status":0,"message":"Student Not Found"},
                            status=status.HTTP_404_NOT_FOUND)
        

    def patch(self,request,id):
        try:
            student=Student.objects.get(id=id)
            serializer = StudentSerializer(student,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":1,"message":"Student Data Updated Successfully",
                                 "data":serializer.data},status=status.HTTP_200_OK)
            return Response({"status":0,"message":serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({"status":0,"message":"Student Not Found"},
                            status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,id):
        try:
            student=Student.objects.get(id=id)
            student.delete()
            return Response({'status':1,'message':'Data deleted successfully'},
                            status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({"status":0,"message":"Student Not Found"},
                            status=status.HTTP_404_NOT_FOUND)

class Registration(APIView):

    def post(self,request):
          serializer = UserSerializer(data=request.data)
          if serializer.is_valid():
              serializer.save()
              user = User.objects.get(username =serializer.data['username'])
              token, created = Token.objects.get_or_create(user=user)
              return Response({"status":1,"message":"User Registered Successfully",
                               "token":str(token),
                               "data":serializer.data},status=status.HTTP_200_OK)
          return Response({"status":0,"message":serializer.errors},
                          status=status.HTTP_400_BAD_REQUEST)
    


class StudentGeneric(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get (self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class StudentGeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'