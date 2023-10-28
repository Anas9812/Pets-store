from django.shortcuts import render,redirect
from .models import cart
from petsapp.models import Pets
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Sum
# Create your views here.


def add_to_cart(request,id):
    cart_id = request.session.session_key
    if cart_id == None:
        cart_id = request.session.create()
    pet_data = Pets.objects.get(id=id)
    price = pet_data.price
    user_data = request.user # fetching user data
    cart(cart_id=cart_id, pet=pet_data,user=user_data,totalPrice=price).save()  # saving the data
    messages.success(request,"Item Added To Cart Successfully")  #message display
    return redirect('/')

def cart_home(request):
    all_items = cart.objects.filter(user=request.user)
    flag = all_items.exists()  # exits = boolean value denga i:e- TRUE OR FALSE
    return render(request,'cart/cart_home.html',{'items':all_items,'flag':flag})

def delete_item(request,id):
    delete_item = cart.objects.get(id=id)
    delete_item.delete()
    messages.success(request,"Item Removed From Cart Successfully")
    return redirect('cartpage')

def update_cart(request,id):
    # print('ID is',id)
    p = request.POST.get('price')
    # price("Price",p)
    q = request.POST.get('qty')
    # print("qty",q)
    p_id = request.POST.get('id')
    total_price = float(p) *int(q)
    cart.objects.filter(id=p_id).update(quantity=q,totalPrice=total_price)
    total_amount = cart.objects.filter(user=request.user).aggregate(total=Sum('totalPrice'))['total']or 0.0
    # total_amount = float(request.session.get('totalamount))
    return JsonResponse({'status':True,'totalprice':total_price})
