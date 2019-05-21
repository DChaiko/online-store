from django.urls import path, include
from django.contrib import admin
from cart.views import CartView




urlpatterns = [
    path('cart_view/', CartView.as_view(), name = 'cart-view'),
    
]
