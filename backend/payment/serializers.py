from rest_framework import serializers
from .models import StudentEntrollment


class StudentEnrollmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= StudentEntrollment
        fields=['id','course','order_amount','payment_id','student','entrolled_time','isPaid'] 