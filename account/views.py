from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,FormView,CreateView,ListView,TemplateView,DetailView
from .forms import*
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import  never_cache
from django.utils.decorators import method_decorator
from account .models import Personaldata,Shippingdata,store,CourierGoods,Booking




from django.utils import timezone
from datetime import timedelta


# Create your views here.
class EHomeView(FormView):
    template_name="home.html"
    form_class=LoginForm
    def post(self,request,*args,**kwrgs):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            us = form_data.cleaned_data.get("username")
            pswd = form_data.cleaned_data.get("password")
            user=authenticate(request,username=us,password=pswd)
            if user:
                login(request,user)
                return redirect('h')
            else:
                messages.error(request,"sign in faild")
                return redirect("home")
        return render (request,"home.html",{"form":form_data})
    
class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=User
    success_url=reverse_lazy("home")
    

class CustHome(View) :
    def get(self,request):
        return render(request,"cust_home.html")
class AboutHome(View):
    def get(self,request) :
        return render(request,"abouts.html") 
class ServiceHome(View):
    def get(self,request) :
        return render(request,"services.html")
    

class PersonaldataView(TemplateView):
    template_name="contact.html"
    def post(self,request,*args,**kwargs):
        
        first=request.POST.get("name1")
        last=request.POST.get("name2")
        email=request.POST.get("subject")
        phone=request.POST.get("phn")
        msg=request.POST.get("message")
        Personaldata.objects.create(firstname=first,lastname=last,email=email,phn=phone,message=msg)
        x=Personaldata.objects.latest('id')
        print(x)
        return redirect('ship',id=x.id)
        
   
   
    
class ShipHome(TemplateView):
   
    template_name="shippingdata.html"
    def post(self,request,id):
        
        p=Personaldata.objects.get(id=id)
        print(p)
        user=request.user
        goodscaty=request.POST.get("goods")
       
        delcity=request.POST.get("city")
        shipaddr=request.POST.get("addr")
        Shippingdata.objects.create(person=p,user=user,Goodscategory=goodscaty, delcity=delcity,shippingaddr=shipaddr)
        x=Shippingdata.objects.latest('id')

        return redirect("calculate_price",id=x.id)
    

    
def calculate_price(request,id):
    
    if request.method=='POST':
        p=Shippingdata.objects.get(id=id)
        Weight=float(request.POST['Weight'])
        CourierGoods.objects.create(shiip=p,Weight=Weight)
        x=CourierGoods.objects.latest('id')
        base_price=0
        price_per_kg=5
        total_price=base_price+(Weight*price_per_kg)
        
        return render(request,'price_result.html',{'total_price':total_price,'id': x.id})
    return render(request,'calculate_price.html')


    

class BookingView(ListView):
    template_name="bookings.html"
    queryset=Booking.objects.all()
    context_object_name="book"

class StoreView(ListView):
    template_name="store.html"
    queryset=store.objects.all()  
    context_object_name='data' 

class LgOutView(View):
    def get(self,request):
        logout(request) 
        return redirect("home")   




class PaymentHome(TemplateView):
    template_name="payment.html"

  
    def post(self,request,id):
        p=CourierGoods.objects.get(id=id)
        u=request.user
        Booking.objects.create(detail=p,user=u)
        
        messages.success(request,"order placed successfully")
        return redirect("h")
     


    


