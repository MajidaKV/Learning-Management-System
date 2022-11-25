
from urllib import response
from django.shortcuts import render
from requests import request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import exceptions
from payment.models import Order
from tutor.serializers import ChapterSerializer, PostCertificateSerializer, QuizAnswerSerializer, QuizQuestionSerializer, QuizSerializer, userAssignmentSerailizer

from tutor.models import Assignments, Certificate, Chapter, Course, PostCertificate, Quiz, QuizQuestions, UserQuizAnswers

from .authentication import JWTUserAuthentication, create_access_token

from .serializers import CourseSerializer, RecomentedCourseSerializer, StudentSerializer, VerifyOtpSerializer
from .  models import Account, Marks, TotalMarks, UserToken
from rest_framework import status
from django.contrib.auth.hashers import check_password

from .verify import send,check
from django.db.models import Q
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.decorators import api_view,permission_classes,authentication_classes

# Create your views here.
class StudentRegisterView(APIView):
    
    def post(self, request, format=None):
        data=request.data
        print(data)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            mobile=data['mobile']
            print(mobile)
            send(mobile)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentRegisterVerification(APIView):
    def post(self,request):
        try:
            data=request.data
            mobile=data['mobile']
            code=data['code']
            if check(mobile,code):
                print('hello')
                user = Account.objects.get(mobile=mobile)   
                print(user)       
                user.is_active= True
                user.save()
                serializer = VerifyOtpSerializer(user, many=False)
                return Response(serializer.data)
            else:
                message = {'detail':'otp is not valid'}
                
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        except:
            message = {'detail':'something went wrong'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class StudentLoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password= request.data['password']

        user=Account.objects.filter(email=email).first()
        if user is None:
            raise exceptions.AuthenticationFailed('Invalid credentials')
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Invalid credential')

        access_token= create_access_token(user.id)
        refresh_token= create_access_token(user.id)


        response = Response()
        response.set_cookie(key='refresh_token', value =refresh_token, httponly=True )
        response.data = {
            'token': access_token
        }

        return response


class StudentView(APIView):
    authentication_classes = [JWTUserAuthentication]
    def get(self,request):
        return Response(StudentSerializer(request.user).data)


class LogoutUserAPIView(APIView):
    def post(self, request):
        refresh_token=request.COOKIES.get('refresh_token')
        print('************')
        print(refresh_token)
        print('***********')
        UserToken.objects.filter(token=refresh_token).delete()
        
        response = Response()
        try:
            response.delete_cookie(key='refresh_token')
            response.delete_cookie(key='phone_number')
        except:
            response.delete_cookie(key='refresh_token')
        response.data={
            'message':'Now you are logout'
        }
        return response
        


class RecomentedCourses(APIView):
    def get(self,request,id):
        
        student=Account.objects.get(pk=id)
        queries=[Q(category__title__iendswith=value) for value in student.interests]
        query=queries.pop()
        for item in queries:
            query != item
        courses = Course.objects.filter(query)
        serializer = RecomentedCourseSerializer(courses,many=True)
        
        return Response (serializer.data)


class getCourse(APIView):
    def get(self,request):
        
        
        courses = Course.objects.all()
        serializer = CourseSerializer(courses,many=True)
        
        return Response (serializer.data)

class CourseDetails(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTUserAuthentication]
    
    def get(self,request,id):
       
        course = Course.objects.filter(pk=id)
        serializer = CourseSerializer(course,many=True)
        
        return Response (serializer.data)


@api_view(['GET'])
@authentication_classes([JWTUserAuthentication])
# permission_classes=[IsAuthenticated]
def AllChapter(request,id):
    users=request.user
    print(users.id)
    print(users)
       
    names=Order.objects.filter(user=users,order_course=id,isPaid=True).first()
    print(names)
    if names:
        course=Course.objects.get(id=id)
        print(course)
        s=course.id
        chapterr=Chapter.objects.filter(course=s)
        serializer=ChapterSerializer(chapterr,many=True)
        return Response(serializer.data)
    else:
        status=Course.objects.filter(id=id,is_Paid=False).first()
        print(status)
        print(status.id)
        if status:
            chapter=Chapter.objects.filter(chapter_no=1,course=status.id)
            print(chapter)
            serializer=ChapterSerializer(chapter,many=True)
            return Response(serializer.data)
        return Response("there is no course")

@api_view(['GET'])
@authentication_classes([JWTUserAuthentication])
# permission_classes=[IsAuthenticated]
def AllAssignments(request,id):
    users=request.user
    print(users.id)
    print(users)
       
    names=Order.objects.filter(user=users,order_course=id,isPaid=True).first()
    print(names)
    if names:
        course=Course.objects.get(id=id)
        print(course)
        s=course.id
        assignment=Assignments.objects.filter(course=s)
        serializer=ChapterSerializer(assignment,many=True)
        return Response(serializer.data)
    else:
        
        return Response("You have to purchase this course")       


@api_view(['POST'])  
@authentication_classes([JWTUserAuthentication])
def UserPostAssignment(request):
    
    users=request.user
    print(users.id)
    print(users)
    data=request.data
    print(data)
    users=Order.objects.filter(user=users,isPaid=True)
    print(users,"check order")
    # for i in users:
    #     print (i.order_course)
    serializer = userAssignmentSerailizer(data=data)
    print('***************66666666666666666666***************')
    print(serializer)
    if serializer.is_valid():
        print('__________6666666666666666_______')
        serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    else:
        return Response("please add correct details")


@api_view(['GET'])  
@authentication_classes([JWTUserAuthentication])       
def GetQuiz(request,id):
    users=request.user
    print(users.id)
    print(users)
       
    names=Order.objects.filter(user=users,order_course=id,isPaid=True).first()
    print(names)
    if names:
        course=Course.objects.get(id=id)
        print(course)
        s=course.id
        assignment=Quiz.objects.filter(course=s)
        serializer=QuizSerializer(assignment,many=True)
        return Response(serializer.data)
    else:
        
        return Response("You have to purchase this course")    

@api_view(['GET'])  
@authentication_classes([JWTUserAuthentication])       
def GetQuizQuestions(request,id):
    user=purchaseCourse=Order.objects.filter(user=request.user,isPaid=True)
    print(purchaseCourse)
    if user:
        questions=QuizQuestions.objects.filter(quiz=id)
        print(questions)
        serailzer=QuizQuestionSerializer(questions,many=True)
    return Response(serailzer.data)

@api_view(['POST'])  
@authentication_classes([JWTUserAuthentication])
def userPostAnswer(request,id):
    # user=purchaseCourse=Order.objects.filter(user=request.user,isPaid=True)
    try:
        user=Order.objects.filter(user=request.user,isPaid=True)
        # print(purchaseCourse)
        data=request.data
        if user:
            
            answer=QuizQuestions.objects.filter(quiz__id=id)
            
            
            totalmarks=0
            
            # print(mark,'printappendfirst')
            if not UserQuizAnswers.objects.filter(question_no=data['question_no']).exists():
                
                if QuizQuestions.objects.filter(id=data['question_no']):
                    serializer=QuizAnswerSerializer(data=data)
                    print(serializer)
                    if QuizQuestions.objects.filter(right_ans=data['answer']):
                        
                        totalmarks+=10
                        print('******************')
                        
                        
                    else:
                        pass
                    if serializer.is_valid():
                        serializer.save()
                        marksss = Marks.objects.create(user=request.user,
                                                    mark=totalmarks,question_no=request.data['question_no'],Quiz=request.data['QuizQuestions'])
                        print(marksss)
                        #print
                        mrks=Marks.objects.filter(mark=10)
                        print(mrks)
                        total=[]
                        for i in mrks:
                            print(i.mark)
                            total.append(i.mark)
                        print(total)
                        s=sum(total)
                        totamarks=TotalMarks.objects.create(
                            user=request.user,
                            totalmark=s
                        )
                        print(sum(total))
                        print('###################')
                        print(totamarks)
                                
                        return Response(serializer.data)
                    else:
                        return Response("something went wrong")
                else:
                     return Response("please add correct question number")
            else:
                # print(mark,'printappendlast')
                return Response("You already answered  this question")
        else:
            return Response("please add correct details")
    except:
        return Response("something went wrong")
            
@api_view(['GET'])  
@authentication_classes([JWTUserAuthentication])  
def ApplyCertificate(request,id):
    user=request.user
    print(user,'uuu')
    users=Order.objects.filter(order_course=id,user=request.user,isPaid=True)

    if users:
        print('************************')
        print(users)
        print('************************')
        
        print(users.values())
        for i in users:
            s=i.user_id
        if s==user.id:
            print('kkkkkkkkkkkkk')
    
        try:
            if Quiz.objects.filter(course=id):
                
                    userintotal=TotalMarks.objects.filter(user=request.user).last()
                    print(userintotal.totalmark)
                    
                    if int(userintotal.totalmark)>=int(90):
                        print("elegible")
                        if not Certificate.objects.filter(username=request.user).exists():
                            certificate=Certificate.objects.create(
                                username=request.user,
                                is_eligible=True,
                                course=id
                            )
                            return Response("You are eligible for certficate")
                        else:
                            return Response("you are allredy applied,certicate is processing")
                    else:
                        return Response("You are not eligible for certficate")
            else:
                return Response("please attend quiz")
        except:
            return Response("please attend quiz..........................")
    else:
            return Response("please pay the course")
    
       
    
@api_view(['GET'])  
@authentication_classes([JWTUserAuthentication])   
def GetCertificate(request,id):
    user=request.user.id
    print(user)
    users=PostCertificate.objects.filter(success=True,course=str(id))
    print(users)
    if users:
        serailzer=PostCertificateSerializer(users,many=True)
        return Response(serailzer.data)
    else:
        return Response("not found certificate")    