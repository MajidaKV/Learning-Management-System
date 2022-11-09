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
from rest_framework.decorators import api_view,authentication_classes

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
        
        teacher=request.user
        print(teacher)
        
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

class CategoryRequestView(APIView):
    permission_classes=[AllowAny]
    
    def post(self, request):
        data=request.data
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            title=data['title']
            print(title)
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    
    serializer_class = CourseSerializer




class TeacherCourseView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        tutor_id = self.kwargs['tutor_id']
        teacher = Teacher.objects.get(pk=tutor_id)
        return Course.objects.filter(teacher=teacher)




@api_view(['POST'])
@authentication_classes([JWTTutorAuthentication])
def addCourse(request):
    data=request.data
    tutor=request.user
    
    teacher=data['teacher']
    
    if str(tutor.id)==str(teacher):
        
        serializer = CreateCourseSerializer(data=data)
        
        
        if serializer.is_valid():
            
            serializer.save()
            message = {'detail':'course added Successfuly'}
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response('you are not allowed')


@api_view(['PATCH'])
@authentication_classes([JWTTutorAuthentication])
def updateCourse(request,id):
    data=request.data
    tutor=request.user
    teacher=data['teacher']
    instance=Course.objects.get(id=id)
    
    if str(tutor.id)==str(teacher):
        
        serializer=CreateCourseSerializer(instance=instance,data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
           
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('course updation is not working')

@api_view(['DELETE'])
@authentication_classes([JWTTutorAuthentication])
def deleteCourse(request,id):
    tutor=request.user
    course=Course.objects.get(id=id)
    
    if tutor.id:
        course.delete()
        return Response('your course was deleted')
    else:
        return Response('course deletion is not working')


@api_view(['POST'])
@authentication_classes([JWTTutorAuthentication])
def addChapter(request):
    data=request.data
    tutor=request.user
    print(tutor)
    course=Course.objects.get(id=data['course'])
    print(data['title'])
    if not Chapter.objects.filter(course=course,title=data['title']).exists():
        if course.teacher==tutor:
                         
            serializer=ChapterSerializer(data=data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response('this course not in your course list')
    else:
            return Response('not allowed')
@api_view(['GET'])
@authentication_classes([JWTTutorAuthentication])
def getChapter(request):
    data=request.data
    tutor=request.user
    print(tutor)
    
    
    
    serializer=ChapterSerializer(data=data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()      
        return Response(serializer.data, status=status.HTTP_200_OK)
    