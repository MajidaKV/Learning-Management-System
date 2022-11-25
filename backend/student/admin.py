from django.contrib import admin

from . import models 

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','mobile','qualification','is_active','interests')
class MarksAdmin(admin.ModelAdmin):
    list_display = ('id','mark','user','Quiz','question_no')

admin.site.register(models.Account,UserAdmin)
admin.site.register(models.Marks,MarksAdmin)




