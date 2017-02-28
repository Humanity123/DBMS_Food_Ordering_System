from django.contrib import admin
from .models import CustomUser, Menu, Order, OrderDetails, Cart

admin.site.register(CustomUser)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(Cart)
# Register your models here.
