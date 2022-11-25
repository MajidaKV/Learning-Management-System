from django.urls import path
from .import views


urlpatterns = [
    path('student_registration/', views.StudentRegisterView.as_view()),
    path('verify_student/',views.StudentRegisterVerification.as_view()),
    path('student_login/', views.StudentLoginView.as_view()),
    path('student/', views.StudentView.as_view()),
    path('student_logout/',views.LogoutUserAPIView.as_view()),
    
    path('recomented_courses/<int:id>/',views.RecomentedCourses.as_view()),
    path('get_course/',views.getCourse.as_view()),
    path('course_details/<int:id>/',views.CourseDetails.as_view()),
    
    path('get_chapter/<int:id>/',views.AllChapter),
    path('get_assignments/<int:id>/',views.AllAssignments),
    path('usesrpostassignment/',views.UserPostAssignment,name='UserPostAssignment'),
    path('get_quiz/<int:id>/',views.GetQuiz),
    path('get_quiz_questions/<int:id>/',views.GetQuizQuestions),
    path('userPostAnswer/<int:id>/',views.userPostAnswer,name='userPostAnswer'),

    path('apply_certificate/<int:id>/',views.ApplyCertificate,name="applycertificate"),
    path('get_certificate/<int:id>/',views.GetCertificate,name="GetCertificate"),

]