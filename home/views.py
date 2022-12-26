from django.shortcuts import render,redirect




from django.contrib import messages
from datetime import datetime

from home.models import Contact


from home.models import User

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from home.models import Cartitems, Customer, Product, Cart
from django.http import JsonResponse
import json

from home.models import Table

# Create your views here.


def index(request):
    
    return render(request, 'index.html')
    

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc= request.POST.get('desc')
        contact = request.POST.get('contact')

        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent!. ')
   
        
    return render(request, 'contact.html') 


def signup(request):
	
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        user=User.objects.create_user(username, email, password)
	
         
    return render(request, 'register.html')	


def user_login(request):
    if request.method == 'POST':

       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(request, username=username, password=password)
       if user is not None:
        login(request, user)

        messages.success(request,'Login successfull! ')
        return redirect('home')

       else:
        messages.success(request,'invalid user name & password')
        redirect('/login')
    return render(request,'login.html')  


def signout(request):
    context={}

    logout(request)

    context['error']="you have been logged out"
    return render(request, 'login.html',context)

def cart(request):
    
    return render(request,'cart.html')


def checkout(request):
    return render(request, 'checkout.html', {})  


def updateCart(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    product = Product.objects.get(id=productId)
    customer = request.user.customer
    cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
    cartitem, created = Cartitems.objects.get_or_create(cart = cart, product = product)

    if action == "add":
        cartitem.quantity += 1
        cartitem.save()
    

    return JsonResponse("Cart Updated", safe = False)


def updateQuantity(request):
    data = json.loads(request.body)
    quantityFieldValue = data['qfv']
    quantityFieldProduct = data['qfp']
    product = Cartitems.objects.filter(product__name = quantityFieldProduct).last()
    product.quantity = quantityFieldValue
    product.save()
    return JsonResponse("Quantity updated", safe = False)  

def store(request):
    if request.user.is_authenticated:
  
   
      return render(request, 'store.html')
    else:
        return render(request, 'login.html')  




    

def booktable(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date= request.POST.get('date')
        time = request.POST.get('time')
        people = request.POST.get('people')
        message = request.POST.get('message')

        booktable=Table(name=name,email=email,phone=phone,date=date,time=time,people=people,message=message)
        booktable.save() 
        messages.success(request,'Your Table book  has been Book!.')
    return render(request, 'booktable.html') 

