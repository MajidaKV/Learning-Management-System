from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Account
from student.serializers import StudentSerializer
from tutor.serializers import TeacherSerializer

from tutor. models import Teacher
from .serializers import UpdateTeacherSerializer, UpdateUserSerializer
from student.authentication import JWTUserAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

# Create your views here.



class VerifyTeacher(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes=[JWTUserAuthentication]
    
    def patch(self,request,id):
        details = Teacher.objects.get(id=id)
        if details.is_active == False:
            details.is_active = True
        else:
            details.is_active= False
        serializer = UpdateTeacherSerializer(details,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            print("teacher verified")
            return Response(serializer.data)
        else:
            print('teacher action failed')
            print(serializer.errors)
            return Response(serializer.errors)

class BlockTeacher(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def patch(self, request,id):
        details = Teacher.objects.get(id=id)
        if details.is_tutor==True:
            details.is_active=False
            details.is_tutor=False
            
        else:
            details.is_tutor=True
            details.is_active=True
        print(details.is_active)
        serializer = UpdateTeacherSerializer(details,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            print(" teacher action Success")
            return Response(serializer.data)
        else:
            print("teacher action failed")
            print(serializer.errors)
            return Response(serializer.errors)

class GetTeachersView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    serializer_classes = TeacherSerializer
    def get(self, request):
    
        vendors = Teacher.objects.all()
        serializer = TeacherSerializer(vendors,many=True)   
        return Response(serializer.data)

class GetTeacherDetailsView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    serializer_classes = TeacherSerializer
    def get(self, request,id):
        try:
            vendor = Teacher.objects.get(id=id)
            serializer = TeacherSerializer(vendor,many=False)   
            return Response(serializer.data)
        except:
            message = {'message':'No User with this id already exist'}
            return Response(message)



class GetUsersView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    serializer_classes = StudentSerializer
    def get(self, request):
    
        users = Account.objects.all()
        serializer = StudentSerializer(users,many=True)   
        return Response(serializer.data)

class GetUserDetailsView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    serializer_classes = StudentSerializer
    def get(self, request,id):
        try:
            user = Account.objects.get(id=id)
            serializer = StudentSerializer(user,many=False)   
            return Response(serializer.data)
        except:
            message = {'message':'No User with this id already exist'}
            return Response(message)  


class BlockUser(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def patch(self, request,id):
        details = Account.objects.get(id=id)
        if details.is_active == True:
            details.is_active=False
        else:
            details.is_active=True
        print(details.is_active)
        serializer = UpdateUserSerializer(details,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            print("action Success")
            return Response(serializer.data)
        else:
            print("action failed")
            print(serializer.errors)
            return Response(serializer.errors)