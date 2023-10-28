from django.urls import path
from .import views

app_name = 'ordersapp'

urlpatterns = [
    path('order_billing/', views.place_order, name='order_billing'),
    path('payment/', views.payment, name='payment')
]



