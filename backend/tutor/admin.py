from django.contrib import admin
from . import models 
# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','dp','email','phone_number','qualification','is_active')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','category','teacher','title','description','image','technology')
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('id','course','chapter_no','title','description','video','material_1','material_2','remarks')

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('id','course','title','description','assignment_file')

class QuizAdmin(admin.ModelAdmin):
    list_display = ('id','teacher','course','title','detail','add_time')  

class QuizQuestionsAdmin(admin.ModelAdmin):
    list_display = ('id','quiz','questions','ans1','ans2','ans3','ans4','right_ans','add_time') 

  

class AdminUserAssignment(admin.ModelAdmin):
    model=models.UserAssignment
    list_display = ('id','userassignment','assignmentsname','studentname','tutorname','coursename')   

class UserQuizAnswersAdmin(admin.ModelAdmin):
    model=models.UserQuizAnswers
    list_display=('id','QuizQuestions','question_no','studentname','answer')

class CertificateAdmin(admin.ModelAdmin):
    model=models.UserQuizAnswers
    list_display=('id','username','is_eligible','course')

class PostCertificateAdmin(admin.ModelAdmin):
    model=models.PostCertificate
    list_display=('id','certificate','usercertificate','success','course')



admin.site.register(models.Teacher, TeacherAdmin)
admin.site.register(models.CourseCategory,CategoryAdmin)
admin.site.register(models.Course,CourseAdmin)
admin.site.register(models.Chapter,ChapterAdmin)
admin.site.register(models.Assignments,AssignmentAdmin)
admin.site.register(models.Quiz,QuizAdmin)
admin.site.register(models.QuizQuestions,QuizQuestionsAdmin)
admin.site.register(models.UserQuizAnswers,UserQuizAnswersAdmin)
admin.site.register(models.UserAssignment,AdminUserAssignment)

admin.site.register(models.Certificate,CertificateAdmin)
admin.site.register(models.PostCertificate,PostCertificateAdmin)