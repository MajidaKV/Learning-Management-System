from django.contrib import admin
from . import models 
# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','email','phone_number','qualification','is_active')


admin.site.register(models.Teacher, TeacherAdmin)
admin.site.register(models.CourseCategory)
admin.site.register(models.Course)
