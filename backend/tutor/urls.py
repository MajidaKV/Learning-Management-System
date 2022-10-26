from django.urls import path
from .import views


urlpatterns = [
    path('teacher_registration/', views.TeacherRegisterView.as_view()),
    path('teacher_login/',views.TeacherLoginView.as_view()),
    path('teacher/',views.TeacherAPIView.as_view()),
    path('teacher_logout/',views.LogoutTeacherAPIView.as_view()),

]