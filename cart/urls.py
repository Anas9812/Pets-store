from django.urls import path
from .views import add_to_cart,cart_home,delete_item,update_cart

urlpatterns=[
    path('add_to_cart/<int:id>',add_to_cart,name='add_to_cart'),
    path('cartpage',cart_home,name='cartpage'),
    path('delete_item/<int:id>',delete_item,name='delete_item'),
    path('updatecart/<int:id>/',update_cart,name='updatecart'),
]