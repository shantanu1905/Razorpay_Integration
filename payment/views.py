from django.shortcuts import render
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Payments
import razorpay
from decouple import config

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.


def index(request):
   return render(request , "index.html")



def home(request):
  if request.method == "POST":
    name= request.POST['name']
    amount= int(request.POST['amount'])*100
    email= request.POST['email']
  

    client = razorpay.Client(auth=(config('razorpay_privatekey'), config('razorpay_publickey')))
    payment = client.order.create({'amount': amount, 'currency': 'INR','payment_capture': '1'})
    print(payment)
    payment_data=Payments(name=name,amount=amount,payment_id=payment['id'],email=email)
    payment_data.save()
  
    messages.success(request, 'Your Request is being processed . click on pay with Razorpay to  proceed')


    
   #email section
    subject = 'Razopay_django_Intregration@<no-reply>'
    html_content =render_to_string("email.html",{'title':'Conformation mail', 'name':name , 'amount':amount , 'email':email })
    text_content =strip_tags(html_content)

    email=EmailMultiAlternatives(
            #subject
            "Razopay_django_Intregration@<no-reply>",
            #content
            text_content,
            #from email
            "shantanunimkar19@gmail.com",
            #rec_list
            [email])
    email.attach_alternative(html_content,"text/html")
    email.send()
        
   
    return render(request, 'home.html' , {'payment':payment })

  return render(request , "home.html")



def success(request):
  if request.method == "POST":
    a=request.POST
    order_id=""
    for key , val in a.items():
      if key=='razorpay_order_id':
        order_id = val
        break
    user=Payments.objects.filter(payment_id=order_id).first()
    user.paid = True
    user.save()
    print(order_id)
    

  return render(request, 'success.html')