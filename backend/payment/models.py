from django.db import models
from student.models import Account
from tutor.models import Course
# Create your models here.
class Order(models.Model):
    
    user =models.ForeignKey(Account,on_delete=models.CASCADE,null =True)
    order_course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    order_amount = models.CharField(max_length=500)
    order_id = models.CharField(max_length=100,blank=True)
    order_payment_id = models.CharField(max_length=100)
    isPaid = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True,null=True)
   
    updated_at = models.DateTimeField(auto_now=True)
    order_status     =models.BooleanField(default=False)
   
    order_total = models.IntegerField(null=True)
    
    def _str_(self):
        return str(self.id)
    
    

class AdminPercentage(models.Model):
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE,null =True)
    Totalamount=models.IntegerField()
    percentage=models.IntegerField(default=12)
    adminPercentageamount=models.IntegerField()
    
   