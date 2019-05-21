from django.contrib import admin
from order.models import Order
from order.models import Status

# Register your models here.

admin.site.register(Order)
admin.site.register(Status)