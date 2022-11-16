from django.contrib import admin
from . import models 

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','mobile','qualification','is_active','interests')
admin.site.register(models.Account,UserAdmin)