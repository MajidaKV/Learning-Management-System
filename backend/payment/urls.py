from django.urls import path
from .import views


urlpatterns = [
   path('payment/',views.Payment,name="payment"),
   path('status/',views.paymentstatus,name="status"),
]