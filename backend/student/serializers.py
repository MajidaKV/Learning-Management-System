from rest_framework import serializers

from tutor.models import Course
from . import models
from .models import Account

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields=['username','email','mobile','password','qualification','is_active','interests']
        extra_kwargs = {
            'email' : {'required': True, 'write_only': True},
            'password' : {'write_only': True}
        }

    def create(self, validated_data) :
        user = Account(
            username = validated_data['username'],
            email = validated_data['email'],
            mobile = validated_data['mobile'],
            qualification = validated_data['qualification'],
            interests = self.validated_data['interests'],
            
        )
        
        user.set_password(validated_data['password'])
        user.save()
        return user

class VerifyOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['is_active']  

class RecomentedCourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Course
        fields=['id','category','teacher','title','description','image','technology'] 

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Course
        fields=['id','category','teacher','title','description','image','technology']
          