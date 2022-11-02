from django.contrib import admin
from . import models 

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','email','mobile','qualification','is_active')
admin.site.register(models.Account,UserAdmin)