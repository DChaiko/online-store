from django.urls import path, include
from django.contrib import admin
from order.views import OrderCreate
from order.form import OrderForm




urlpatterns = [
    path('order/', OrderCreate.as_view(), name = 'order-create'),
    
]


