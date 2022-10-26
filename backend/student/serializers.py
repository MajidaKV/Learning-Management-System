from rest_framework import serializers
from . import models
from .models import Account

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields=['username','email','mobile','password','qualification']
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
            
        )
        
        user.set_password(validated_data['password'])
        user.save()
        return user

class VerifyOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['is_active']        