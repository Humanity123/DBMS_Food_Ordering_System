from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	address= models.CharField(max_length=200)
	contact = models.CharField(max_length=200)

	type_choices = (
		
		('R', 'Restaurant'),
		('C', 'Customer'),
		
	)
	user_type = models.CharField(max_length=1,
								 choices=type_choices,
								 default='C')


class Menu(models.Model):
    name = models.CharField(max_length=200)
    restaurant = models.ForeignKey(CustomUser)
    price = models.IntegerField(default=0)

    type_choices = (
		('NI', 'North Indian'),
		('SI', 'South Indian'),
		('FF', 'Fast Food'),
		('C', 'Continental'),
		('B', 'Beverage'),
		('D', 'Desset'),
	)
    category = models.CharField(max_length=2,
								 choices=type_choices,
								 default='C')
    
   
    def __str__(self):
        return self.name

class Order(models.Model):
    orderid = models.IntegerField(primary_key = True)
    type_choices = (
		
		('P', 'Under Preparation'),
		('O', 'Dispatched'),
		('D', 'Delivered'),
		
	)
    status= models.CharField(max_length=1,
								 choices=type_choices,
								 default='P')
   
    customer = models.ForeignKey(CustomUser, related_name='c')
    restaurant = models.ForeignKey(CustomUser, related_name='r')
    when = models.DateTimeField(null=True)
   
    def __str__(self):
        return str(self.orderid)

class OrderDetails(models.Model):
	order=models.ForeignKey(Order)
	dish=models.ForeignKey(Menu)
	qty=models.IntegerField()
	def __str__(self):
		return str(self.order.orderid)+str("_")+str(self.dish.restaurant.username)+str("_")+str(self.dish.name)



class Cart(models.Model):
	customer=models.ForeignKey(CustomUser)
	dish=models.ForeignKey(Menu)
	qty=models.IntegerField()

# Create your models here.
