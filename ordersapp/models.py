from django.db import models
from petsapp.models import Pets
from django.contrib.auth.models import User


# Create your models here.


class Payment(models.Model):
    payment_id = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_paid = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.payment_id
    
    
    
    
class Orders(models.Model):
    status = (
        ('new','new'),
        ('pending','pending'),
        ('delivered','delivered'),
        ('cancelled','cancelled')
    )
    
    states = [
        ('AP','Andhra Pradesh'),
        ('AR','Arunachal Pradesh'),
        ('MH','Maharashtra'),
        ('RJ','Rajasthan'),
        ('UP','Uttar Pradesh'),
        ('GJ','Gujrat'),
        ('AS','Assam'),
        ('BR','Bihar')
    ]
    
  
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.SET_NULL,blank=True,null=True)
    order_number = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state= models.CharField(max_length=100,choices=states)
    country = models.CharField(max_length=100)
    total = models.FloatField()
    status = models.CharField(max_length=100,choices=status,default='new')
    ip = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)  # [for new object] banega usko track karne ke liye auto_now_add use karenge
    updated_at = models.DateTimeField(auto_now=True)  # for already created objects (jo pehele se bana objects hai uske liye auto_no use karte )
    
    
    
    def __str__(self):
        return self.first_name
    
    
    
class OrderPet(models.Model):
    order_id = models.ForeignKey(Orders,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.SET_NULL,blank=True,null=True)
    pet = models.ForeignKey(Pets,on_delete=models.CASCADE)
    quantity = models.FloatField()
    pet_price = models.FloatField()
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.pet.name
    
    
    
    
    # website username and password 
    
    # username =  sirpunit123
    # register password = itvedant123 
    
    
    # admin panel username and password
    
    # username = Anas123
    # password = itvedant123