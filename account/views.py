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
        id= kwargs.get("id")
        
        first=request.POST.get("name1")
        last=request.POST.get("name2")
        email=request.POST.get("subject")
        phone=request.POST.get("phn")
        msg=request.POST.get("message")
        Personaldata.objects.create(firstname=first,lastname=last,email=email,phn=phone,message=msg)
        # messages.success(request,"order placed successfully")
        return redirect('ship')
        
   
    # def get(self,request):
    #     return render(request,"contact.html")  
    
class ShipHome(TemplateView):
    # def get(self,request,*args,**kwargs):
    #     cid=kwargs.get("id")
    #     product=Personaldata.objects.get(id=cid)
    template_name="shippingdata.html"
    def post(self,request,*args,**kwargs):
        # cid=kwargs.get("id")
        # product=Personaldata.objects.get(id=cid)
    
        goodscaty=request.POST.get("goods")
        shipvalue=request.POST.get("price")
        delcity=request.POST.get("city")
        shipaddr=request.POST.get("addr")
        Shippingdata.objects.create(Goodscategory=goodscaty, delcity=delcity,shippingaddr=shipaddr,shipvalue=shipvalue)
        # product.save()
        return redirect("calculate_price")
    

    
def calculate_price(request):
    
    if request.method=='POST':
        Weight=float(request.POST['Weight'])
        CourierGoods.objects.create(Weight=Weight)
        base_price=0
        price_per_kg=5
        total_price=base_price+(Weight*price_per_kg)
        
        return render(request,'price_result.html',{'total_price':total_price})
    return render(request,'calculate_price.html')


    

class BookingView(ListView):
    template_name="bookings.html"
    queryset=Booking.objects.all()
    context_object_name="book"

class StoreView(ListView):
    # def get(self,request):
    #     res=store.objects.all()
    #     return render(request,"store.html",{"data":res})    
    
    template_name="store.html"
    
    queryset=store.objects.all()  
    context_object_name='data' 

class LgOutView(View):
    def get(self,request):
        logout(request) 
        return redirect("home")   




class PaymentHome(TemplateView):
    template_name="payment.html"

    def post(self,request,*args,**kwargs): 
       
        user=request.user
        phone=request.POST.get("phn")
        Booking.objects.create(user=user,phone=phone)
        messages.success(request,"Booking successful ")
        return redirect("book")


     


    


