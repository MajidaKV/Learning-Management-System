from django.shortcuts import render
import json
import razorpay
from django.conf import settings
from .models import Order
# Create your views here.



def Payment(request):
    payment =0
    order=0
    if request.method == 'POST':
        amount = request.POST.get('amount')
        name = request.POST['name']
        
        request.session['key'] = name
        print(name,'name')
        

        client =razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
        payment = client.order.create({"amount": int(amount) * 100, 
                                   "currency": "INR", 
                                   "payment_capture": "1"})
        print(payment,'this is payment')
        user = request.user
        print(user)
        order = Order.objects.create(order_course_id=name, 
                                 order_amount=amount, 
                                 user=request.user,
                                 order_id=payment['id'])
        payment['name']=name
        print(name)      
        print(order)                                          
       
    
    return render(request,'payments.html',{'payment':payment,'order':order})



def paymentstatus(request):
    status =None
    response = request.POST
   

    print("ddd",response)

    params_dict = {
        'razorpay_order_id':response['razorpay_order_id'],
        'razorpay_payment_id':response['razorpay_payment_id'],
        'razorpay_signature':response['razorpay_signature']
    }

    client =razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))

   
    status = client.utility.verify_payment_signature(params_dict)
    print(status)
    try:
        order = Order.objects.get(order_id=response['razorpay_order_id'])
        order.order_payment_id  = response['razorpay_payment_id']
            
        order.isPaid = True
        order.order_status=True
        order.save()

    
        return render(request,'status.html',{'status':True})
    except:
        return render(request,'status.html',{'status':False})