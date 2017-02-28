from django.contrib import admin
from .models import CustomUser, Menu, Order, OrderDetails

admin.site.register(CustomUser)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderDetails)
# Register your models here.
