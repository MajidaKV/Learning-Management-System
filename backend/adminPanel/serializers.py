from rest_framework import serializers
from student.models import Account
from tutor.models import Teacher



class UpdateTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        extra_kwargs = {
            'password' : {'write_only' : True}
        }


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        extra_kwargs = {
            'password' : {'write_only' : True}
        }        