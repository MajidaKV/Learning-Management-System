from rest_framework import serializers
from . models import Assignments, Chapter, Course, CourseCategory, Quiz, Teacher,QuizQuestions
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
        fields = ['id','category','teacher','title','description','image','technology','price']   
        depth=1     
        
class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','category','teacher','title','description','image','technology','price']

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id','course','chapter_no','title','description','video','material_1','material_2','remarks']
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignments
        fields = ['id','course','title','description','assignment_file']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id','teacher','course','title','detail','add_time']

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestions
        fields = ['id','quiz','questions','ans1','ans2','ans3','ans4','right_ans','add_time']
        extra_kwargs = {
            'right_ans' : {'write_only' : True}
        }