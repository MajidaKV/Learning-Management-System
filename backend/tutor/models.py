from enum import unique
from django.db import models
from django.forms import ImageField

from student.models import Account
# Teacher Model
class Teacher (models.Model):
    
    first_name = models. CharField(max_length = 100)  
    last_name  = models.CharField(max_length=100)
    email = models.CharField(max_length = 100,unique=True)
    password = models.CharField(max_length = 100)
    qualification = models.CharField(max_length = 200)
    skills = models.TextField()
    phone_number = models.CharField(max_length = 20,unique=True)
    address = models.TextField()
    dp              =models.ImageField(upload_to='photos/teachers_dp/',blank=True)


        
    create_date    = models.DateTimeField(auto_now_add=True)
    last_login     = models.DateTimeField(auto_now=True)
    modified_date  = models.DateTimeField(auto_now=True)
    is_tutor     = models.BooleanField(default=True)
    is_Paid        = models.BooleanField(default=False)
    is_active      = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return self.email
    
    
    class Meta:
        verbose_name_plural="1. Teachers" 
        



# Course Category Model
class CourseCategory(models.Model):
    title=models.CharField(max_length=150,unique=True)
    description=models.TextField()

    is_added=models.BooleanField(default=False,blank=True)

    class Meta:
        verbose_name_plural="2. Course Categories"
    def __str__(self):
        return self.title


 
#Course Model
class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField()
    image = models.ImageField(upload_to = 'photos/course_img/',blank=True)
    technology=models.TextField()

    is_Paid        = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural="3. Courses"
    def __str__(self):
        return self.title
#Chapter Model
class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title =models.CharField(max_length=150)
    
    description=models.TextField()
    video = models.FileField(upload_to = 'video/chapter/',blank=True)
    material_1=models.FileField(upload_to = 'material_1/chapter/',blank=True)
    material_2=models.ImageField(upload_to = 'material_2/chapter/',blank=True)
    remarks=models.TextField(null=True)
    class Meta:
        verbose_name_plural="4. Chapters"        
    def __str__(self):
        return self.title

# Assignment model
class Assignments(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title =models.CharField(max_length=150)
    description= models.TextField()
    assignment_file=models.FileField(upload_to = 'assignment/chapter/')

    is_done=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural="5. Assignments"        
    def __str__(self):
        return self.title

# Quiz Models
class Quiz(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=150)
    detail=models.TextField(max_length=150)
    add_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="6.Quiz" 

class QuizQuestions(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True)
    questions=models.CharField(max_length=200)
    ans1=models.CharField(max_length=200)
    ans2=models.CharField(max_length=200)
    ans3=models.CharField(max_length=200)
    ans4=models.CharField(max_length=200)
    right_ans=models.CharField(max_length=200)
    add_time=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural="7.Quiz Questions" 

class CourseQuiz(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True)
    add_time=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural="8.Course Quiz " 


    


class TeacherToken(models.Model):
    tutor_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    def __str__(self):
        return str(self.teacher_id) +' '+ self.token

