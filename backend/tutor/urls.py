from django.urls import path
from .import views


urlpatterns = [
    path('teacher_registration/', views.TeacherRegisterView.as_view()),
    path('teacher_login/',views.TeacherLoginView.as_view()),
    path('teacher/',views.TeacherAPIView.as_view()),
    path('teacher_logout/',views.LogoutTeacherAPIView.as_view()),

    path('category/',views.CategoryView.as_view()),
    path('course/',views.CourseView.as_view()),
    path('add_course/',views.addCourse),
    path('teacher_course/<int:tutor_id>/',views.TeacherCourseView.as_view()),
    path('update_course/<int:id>/',views.updateCourse),
    path('delete_course/<int:id>/',views.deleteCourse),
    path('add_chapter/',views.addChapter),
    
]