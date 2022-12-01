from django.shortcuts import render
from rest_framework.views import APIView
from payment.models import Order
from student.models import Account
from student.serializers import StudentSerializer
from tutor.serializers import TeacherSerializer

from tutor. models import CourseCategory, Teacher
from .serializers import UpdateCategorySerializer, UpdateTeacherSerializer, UpdateUserSerializer, addCategorySerializer
from student.authentication import JWTUserAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework import status

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



@api_view(['POST'])
@permission_classes([IsAdminUser])
@authentication_classes([JWTUserAuthentication])
def addCategory(request):
    data=request.data
        
    serializer = addCategorySerializer(data=data)
    
    if serializer.is_valid():
        
        serializer.save()
        message = {'detail':'category added Successfuly'}
    
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        
        print(serializer.errors)
        return Response(serializer.errors)

class VerifyCategory(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes=[JWTUserAuthentication]
    
    def patch(self,request,id):
        details = CourseCategory.objects.get(id=id)
        if details.is_added == False:
            details.is_added = True
        else:
            details.is_added= False
        serializer = UpdateCategorySerializer(details,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            print("category verified")
            return Response(serializer.data)
        else:
            print('action failed')
            print(serializer.errors)
            return Response(serializer.errors)


class getTotalamount(APIView):
    permission_classes=[IsAdminUser]
    
    def get(self,request):
        amount=Order.objects.filter(isPaid=True)
        print(amount)
        j=0
        for i in amount:
            
            print(type(j))
            s=i.order_amount
            k=int(s)
            print(type(k))
            j=k+j
            print(j)
        print(j)
        return Response(data={"total income":j})


class adminPercentage(APIView):
    permission_classes=[IsAdminUser]
    def get(self,request):
        
        amount=Order.objects.filter(isPaid=True)
        print(amount)
        j=0
        for i in amount:
            
            print(type(j))
            s=i.order_amount
            k=int(s)
            print(type(k))
            j=k+j
            print(j)
            adminperctage=(j*12)/100
            print(adminperctage)
            # AdminPercentage.objects.create(
            #     Totalamount = j,
            #     percentage=12,
            #     adminPercentageamount= adminperctage,
                
            # )
        return Response(data={"Total  Amount":j,"percentage":12,"admin Percentage amount":adminperctage})

class TeacherAmount(APIView):
    permission_classes=[IsAdminUser]
    def get(self,request):
        if Order.objects.filter(isPaid=True):
            teacher=Order.objects.all()
            print(teacher.values())
            s=teacher.values_list('order_course_id')
            print('llllllllllllllllll')
            print(s)
            li=[]
            for i in s:
                
                print(i)
                li.append(i)
            print(li,"appeid list")