from .models import CustomUser
from django.contrib.auth.models import User
from django import forms

class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password' ,'first_name','last_name', 'contact','address')



class RestForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'first_name', 'contact', 'address')

class MenuForm(forms.Form):
    name = forms.CharField(label = 'Name', max_length = 20, required = True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    price = forms.IntegerField(label = 'Price', required = True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    type_choices = [
		('NI', 'North Indian'),
		('SI', 'South Indian'),
		('FF', 'Fast Food'),
		('C', 'Continental'),
		('B', 'Beverage'),
		('D', 'Desset'),]
    category = forms.ChoiceField(choices=type_choices,widget=forms.Select(attrs={'class':'form-control'}), required = True)

class OrderForm(forms.Form):
	# price = forms.IntegerField(label = 'Price', required = True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	type_choices = [
		('NI', 'North Indian'),
		('SI', 'South Indian'),
		('FF', 'Fast Food'),
		('C', 'Continental'),
		('B', 'Beverage'),
		('D', 'Desset'),]

	category = forms.ChoiceField(choices = type_choices, widget=forms.Select(attrs={'class':'form-control'}), required=True)