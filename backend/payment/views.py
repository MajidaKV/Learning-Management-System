from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import StudentEnrollmentSerializer

from .models import StudentEntrollment
from rest_framework.response import Response


# Create your views here.
class PaymentStatus(APIView):
    def get(request,id):
        order = StudentEntrollment.objects.get(id=id)   
        print(order)       
        order.isPaid= True
        order.save()
        serializer = StudentEnrollmentSerializer(order)
        return Response(serializer.data)

