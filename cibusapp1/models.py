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

class Dish(models.Model):
    name = models.CharField(max_length=200)
    
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
# Create your models here.
