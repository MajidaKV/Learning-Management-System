from django.db import models
# Teacher Model
class Teacher (models.Model):
    
    first_name = models. CharField(max_length = 100)  
    last_name  = models.CharField(max_length=100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    qualification = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length = 20)
    address = models.TextField()

        
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
        


class TutorToken(models.Model):
    tutor_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    def __str__(self):
        return str(self.vendor_id) +' '+ self.token

# Course Category Model
class CourseCategory(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()

    class Meta:
        verbose_name_plural="2. Course Categories"
 
#Course Model
class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField()
    class Meta:
        verbose_name_plural="3. Courses"
 
class TeacherToken(models.Model):
    tutor_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    def __str__(self):
        return str(self.teacher_id) +' '+ self.token
