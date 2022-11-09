from rest_framework import serializers
from . models import Chapter, Course, CourseCategory, Teacher
from django.contrib.auth.hashers import make_password

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["first_name","last_name",'email',"phone_number","password","dp"]  

        extra_kwargs = {
            'password' : {'write_only' : True}
        }
    
    def validate_password(self,value):
        if len(value)<6:
            raise serializers.ValidationError("Password must be minimum 6 characters")
        else:
            return value
    def validate_phone_number(self,value):
        if len(value)<10:
            raise serializers.ValidationError("Phonenumber must be minimum 10 digits")
        else:
            return value
    def save(self):
        teacher = Teacher.objects.create(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            phone_number=self.validated_data['phone_number'],
            
            password = make_password(self.validated_data['password']),
            
        )
        print(teacher)
        
        return teacher

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ['id','title','description']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','category','teacher','title','description','image','technology']   
        depth=1     
        
class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','category','teacher','title','description','image','technology']

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id','course','title','description','video','material_1','material_2','remarks']
