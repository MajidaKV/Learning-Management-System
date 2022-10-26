from django.urls import path
from . import views
urlpatterns = [
    path('verify_teacher/<int:id>/',views.VerifyTeacher.as_view()),
    path('blockteacher/<int:id>/',views.BlockTeacher.as_view()),
    path('getteacherdetails/<int:id>/',views.GetTeacherDetailsView.as_view()),
    path('getteachers/',views.GetTeachersView.as_view()),
] 