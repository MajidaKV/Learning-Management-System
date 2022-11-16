from django.db import models

from student.models import Account
from tutor.models import Course

# Create your models here.
class StudentEntrollment(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='entrolled_courses')
    order_amount=models.CharField(max_length=25,blank=True)
    payment_id =models.CharField(max_length=100,blank=True)
    student = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='entrolled_student')
    entrolled_time =models.DateField( auto_now_add=True)
    isPaid = models.BooleanField(default=False)

    def __str__(self):
        return self.order_payment_id
    
   