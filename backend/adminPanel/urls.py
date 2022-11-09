from django.urls import path
from . import views
urlpatterns = [
    path('verify_teacher/<int:id>/',views.VerifyTeacher.as_view()),
    path('blockteacher/<int:id>/',views.BlockTeacher.as_view()),
    path('getteacherdetails/<int:id>/',views.GetTeacherDetailsView.as_view()),
    path('getteachers/',views.GetTeachersView.as_view()),

    path('getuser/',views.GetUsersView.as_view()),
    path('getuserdetails/<int:id>/',views.GetUserDetailsView.as_view()),
    path('blockuser/<int:id>/',views.BlockUser.as_view()),
    
    path('addcategory/',views.addCategory),
    path('verify_category/<int:id>/',views.VerifyCategory.as_view()),
]   