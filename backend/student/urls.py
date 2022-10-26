from django.urls import path
from .import views


urlpatterns = [
    path('student_registration/', views.StudentRegisterView.as_view()),
    path('verify_student/',views.StudentRegisterVerification.as_view()),
    path('student_login/', views.StudentLoginView.as_view()),
    path('student/', views.StudentView.as_view()),
    path('student_logout/',views.LogoutUserAPIView.as_view()),
    
]