from django.contrib import admin
from . import models 

# Register your models here.

class paymentAdmin(admin.ModelAdmin):
    list_display = ('id','user','order_course','order_amount','order_id','order_payment_id','isPaid','order_date')
admin.site.register(models.Order,paymentAdmin)