
from urllib import response
from django.shortcuts import render
from requests import request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import exceptions

from .authentication import JWTUserAuthentication, create_access_token

from .serializers import StudentSerializer, VerifyOtpSerializer
from .  models import Account, UserToken
from rest_framework import status
from django.contrib.auth.hashers import check_password

from .verify import send,check

# Create your views here.
class StudentRegisterView(APIView):
    
    def post(self, request, format=None):
        data=request.data
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
        
