from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions

from .authentication import JWTTutorAuthentication, create_access_token, create_refresh_token
from .serializers import CategorySerializer, ChapterSerializer, CourseSerializer, CreateCourseSerializer, TeacherSerializer
from rest_framework.response import Response
from .  models import Chapter, Course, CourseCategory, Teacher, TeacherToken
from rest_framework.permissions import AllowAny
from rest_framework import status

from django.contrib.auth.hashers import check_password
import datetime
from rest_framework import generics

# Create your views here.
class TeacherRegisterView(APIView):
    permission_classes=[AllowAny]
    
    def post(self, request):
        data=request.data
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            mobile=data['phone_number']
            print(mobile)
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherLoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        print('*****************************')
        print(email,password)
        print('*****************************')
        
        teacher = Teacher.objects.filter(email=email).first()
        print(teacher,"123")
        if teacher is None:
            response = Response()
           
            response.data={
                'message':'Invalid email'
            }
            return response


        storedpassword = str(teacher.password)

        print(password,storedpassword)

        ans = check_password(password, storedpassword)
        print(ans)


        if  not check_password(password, storedpassword) :
            response = Response()
            response.data={
               'message':'Password Inncorect'
            }
            return response  

        if teacher.is_active:
            access_token = create_access_token(teacher.id)
            refresh_token = create_refresh_token(teacher.id)

            TeacherToken.objects.create(
                tutor_id = teacher.id,
                token= refresh_token,
                expired_at =  datetime.datetime.utcnow()+datetime.timedelta(seconds=7),
            )

            response = Response()
            
            response.set_cookie(key='refresh_token',value=refresh_token,httponly=True)
            response.data = {
                'token': access_token,
                
            }
            return response
        else:
            response = Response()
            response.data={
                'message':'Not verifiede teacher'
            }
            return response  


class TeacherAPIView(APIView):
    authentication_classes = [JWTTutorAuthentication]
    def get(self, request):
        print(request)
        print('koooooooooooooooooooyyyyyyyyyyyyyyy')
        teacher=request.user
        print(teacher)
        print('koooooooooooooooooooyyyyyyyyyyyyyyy')
        teacher=Teacher.objects.get(email=teacher.email)
        serializer=TeacherSerializer(teacher,many=False)
        return Response(serializer.data)


class LogoutTeacherAPIView(APIView):
    def post(self, request):
        refresh_token=request.COOKIES.get('refresh_token')
        TeacherToken.objects.filter(token=refresh_token).delete()
        response = Response()
        response.delete_cookie(key='refresh_token')
        response.data={
            'message':'logout'
        }
        return response 

class CategoryView(generics.ListCreateAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CategorySerializer

class CourseView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    
    serializer_class = CourseSerializer

class CreateCourseView(generics.ListCreateAPIView):
    authentication_classes = [JWTTutorAuthentication]
    queryset = Course.objects.all()
    
    serializer_class = CreateCourseSerializer    


class TeacherCourseView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        tutor_id = self.kwargs['tutor_id']
        teacher = Teacher.objects.get(pk=tutor_id)
        return Course.objects.filter(teacher=teacher)

class ChapterView(generics.ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer