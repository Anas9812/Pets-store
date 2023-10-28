from django.shortcuts import render, redirect
from .models import Pets
from django.http import Http404
from django.db.models import Q
from ordersapp.models import OrderPet
#from django.http import HttpResponse

# Create your views here.


def pets_list(request):
    all_products = Pets.objects.all()    #query
    context = {
        'objects': all_products
    }
    return render(request,'petsapp/list.html',context)



def dog_list(request):
    dog_list = Pets.objects.filter(animal_type='D')
    all_dog_data = {
        'objects' : dog_list
    }
    return render(request,'petsapp/doglist.html',all_dog_data)


def cat_list(request):
    cat_list = Pets.objects.filter(animal_type='C')
    all_cat_data = {
        'objects' : cat_list
    }
    return render(request,'petsapp/doglist.html',all_cat_data)




def pet_details(request,pk):
    #user = request.user
    query = Pets.objects.get(id=pk)
    context = {
        'objects' : query
    }
    return render(request,'petsapp/pet_detail.html',context)




def search(request):
    if request.method =="GET":
        search_data = request.GET.get('search')
        if(len(search_data)==0):
            raise Http404
        else:
            query = (Q(name__icontains=search_data) | Q(species__icontains=search_data) | Q(breed__icontains=search_data))
        result = Pets.objects.filter(query)
        context = {
            'objects' : result
        }
        return render(request,'petsapp/search.html',context)
    else :
        raise Http404



'''def home(request):

    return redirect('pet_details')'''
    
    


def order_history(request):
    # user = request.user
    query = OrderPet.objects.filter(user=request.user)
    flag = query.exists()
    status_badge_map = {
        'new': 'primary',
        'pending': 'warning',
        'delivered': 'success',
        'cancelled': 'danger'
    } 

    # Retriving the order data with associated Order Item.
    
    orders = OrderPet.objects.filter(user=request.user).select_related('order_id','pet').order_by('-order_id__created_at')
    #print(76, orders)
    
    order_group = {}
    for order in orders:
        order_number = order.order_id.order_number    #order number
        if order_number not in order_group:
            order_group[order_number] = {
                'order_date' : order.order_id.created_at.date(),
                'status' : order.order_id.status,
                'status_badge_map' : status_badge_map.get(order.order_id.status,'secondary'),
                'order_number' : order_number,
                'grand_total' : 0,
                'items' : []
            }
            
        order_group[order_number]['grand_total']+= order.pet_price
        total_price_per_item = order.quantity * order.pet_price
        order_group[order_number]['items'].append({
            'item_name' : order.pet.name,
            'item_price' : order.pet_price,
            'quantity' : order.quantity,
            'total_price_per_item' : total_price_per_item,
        })
            
    content = {
        'order_group' : order_group.values(),
        'flag' : flag
        }
            
    return render(request,'base/order_history.html', content)
   
        
    
    





