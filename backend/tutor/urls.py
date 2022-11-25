from django.urls import path
from .import views


urlpatterns = [
    path('teacher_registration/', views.TeacherRegisterView.as_view()),
    path('teacher_login/',views.TeacherLoginView.as_view()),
    path('teacher/',views.TeacherAPIView.as_view()),
    path('teacher_logout/',views.LogoutTeacherAPIView.as_view()),

    path('category/',views.CategoryView.as_view()),
    path('category_request/', views.CategoryRequestView.as_view()),
    
    path('course/',views.CourseView.as_view()),
    path('add_course/',views.addCourse),
    path('teacher_course/<int:tutor_id>/',views.TeacherCourseView.as_view()),
    path('update_course/<int:id>/',views.updateCourse),
    path('delete_course/<int:id>/',views.deleteCourse),
    
    path('add_chapter/',views.addChapter),
    #path('get_chapter/',views.getChapter),
    path('update_chapter/<int:id>/',views.updateChapter),
    path('delete_chapter/<int:id>/',views.deleteChapter),

    path('add_assignment/<int:id>/',views.addAssignment),
    path('update_assignment/<int:id>/',views.updateAssignment),
    path('delete_assignment/<int:id>/',views.deleteAssignment),

    path('add_quiz/<int:id>/',views.addQuiz),
    path('assign_quiz/<int:id>/',views.assignQuiz),

    path('teachercheckcertificate/<int:id>/',views.teachercheckcertificate,name="teachercheckcertificate"),
    
    path('postcertificate/<int:id>/',views.Postcertificate,name="PostCertificate"),
    
    
]