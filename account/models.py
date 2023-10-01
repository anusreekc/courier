from django.db import models

from django.contrib.auth.models import User

class Personaldata(models.Model):
   
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField(null=True)
    phn=models.IntegerField(null=True)
    message=models.CharField(max_length=500,null=True)
    
class Shippingdata(models.Model):
    person=models.ForeignKey(Personaldata,on_delete=models.CASCADE,null=True) 
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    options=(
        ('Electronics','Electronics'),
        ('Fasion','Fasion'),
        ('Accessories','Accessories'),
        ('Books','Books'),
        ('Home Appliances','Home Appliances'),
        
    )
    Goodscategory=models.CharField(max_length=200,choices=options,default='Books')
    delcity=models.CharField(max_length=100)
    shippingaddr=models.CharField(max_length=100)
    


class store(models.Model):
    name=models.CharField(max_length=100) 
    address=models.CharField(max_length=500)  
    contact=models.IntegerField(null=True) 


class CourierGoods(models.Model):
    shiip=models.ForeignKey(Shippingdata,on_delete=models.CASCADE,null=True) 
    Weight=models.FloatField(null=True)  
    # user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
  


class Booking(models.Model):
    detail=models.ForeignKey(CourierGoods,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    options=(
        ('Confirmed','Confirmed'),
        ('Shipped','Shipped'),
        ('Order cancelled','Order cancelled'),
        
        
    )
    Status=models.CharField(max_length=200,choices=options,default='Confirmed')










     