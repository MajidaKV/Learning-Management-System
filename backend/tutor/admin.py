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
    list_display = ('id','course','title','description','video','remarks')

admin.site.register(models.Teacher, TeacherAdmin)
admin.site.register(models.CourseCategory,CategoryAdmin)
admin.site.register(models.Course,CourseAdmin)
admin.site.register(models.Chapter,ChapterAdmin)
