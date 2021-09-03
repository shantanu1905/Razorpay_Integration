from django.shortcuts import render
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Payments
import razorpay
# Create your views here.



def home(request):
  if request.method == "POST":
    name= request.POST['name']
    amount= request.POST['amount']
    client = razorpay.Client(auth=("rzp_test_CIlOBrB23fsNUZ", "Wj6irDYmV2sLav62O5pRNeHb"))
    payment = client.order.create({'amount': amount, 'currency': 'INR','payment_capture': '1'})
    print(payment)
   # payment_data=Payments(name=name,amount=amount,payment_id=payment['id'])
   # print(name)
    context = {'payment':payment }
  return render(request, 'home.html', context )



def success(request):
  if request.method == "POST":
    a=request.POST
    print(a)
    

  return render(request, 'success.html')