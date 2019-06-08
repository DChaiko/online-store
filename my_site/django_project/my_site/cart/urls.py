from django.urls import path, include
from django.contrib import admin
from cart.views import CartView, DeleteOrder




urlpatterns = [
    path('cart_view/', CartView.as_view(), name = 'cart-view'),
    path('delete_order/<int:pk>/', DeleteOrder.as_view(), name = 'order-delete'),
    
]
