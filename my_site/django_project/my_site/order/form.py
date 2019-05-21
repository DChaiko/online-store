from django import forms
from django.forms import ModelForm
from order.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['cart', 'status', 'adress', 'email', 'contacts']
        
        
        widgets = {'cart': forms.HiddenInput, 'status': forms.HiddenInput} 