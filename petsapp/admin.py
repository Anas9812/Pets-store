from django.contrib import admin
from .models import Pets 
from django.utils.html import format_html
from ordersapp.models import Orders,Payment, OrderPet
from cart.models import cart




class CustAdmin(admin.ModelAdmin):
    list_display = ['name','gender','age','price','species','description','img_dislay']
    search_fields = ['animal_type','price','species']
    list_filter = ['animal_type','gender']
    list_per_page = 5
    
    def img_dislay(self,obj):
        return format_html ('<img src={} width="90" height= "90"/>',obj.image.url)
    
    
    
    
class Ordercustom(admin.ModelAdmin):
    list_display = ['user','status']
    
class PaymentCustom(admin.ModelAdmin):
    list_display = ['payment_id','status']
    
# Register your models here.
admin.site.register(Pets,CustAdmin) 

admin.site.register(cart)
admin.site.register(Orders, Ordercustom)
admin.site.register(Payment, PaymentCustom)
admin.site.register(OrderPet)