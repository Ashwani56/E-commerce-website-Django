from django.urls import path
from home import views
from django.contrib import admin



urlpatterns = [
    
    path('',views.index,name='home'),
    path('contact',views.contact,name='contact'),
    path('register',views.signup,name='register'),
    path('login',views.user_login,name='login'),
    path('logout',views.signout,name='logout'),
   
    path('checkout',views.checkout,name='checkout'),
    path('store',views.store,name='store'),
    path('booktable',views.booktable,name='booktable'),
  
    
]