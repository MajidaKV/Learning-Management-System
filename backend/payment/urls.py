from django.urls import path
from .import views


urlpatterns = [
   path('course_enrollment/<int:id>/',views.PaymentStatus.as_view())
]