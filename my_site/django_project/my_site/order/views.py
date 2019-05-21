from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from order.form import OrderForm
from order.models import Order
from django.urls import reverse_lazy

# Create your views here.

class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    #fields = ['cart', 'status', 'adress', 'email', 'contacts']

    def get_success_url(self):
        del self.request.session['cart-id']
        return reverse_lazy('home')
