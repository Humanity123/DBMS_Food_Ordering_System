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
    first_name = forms.CharField(label = 'Name of restaurant', max_length = 20, required = True, widget=forms.TextInput(attrs={'class' : 'form-control'}))

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
	type_choices = [
		('NI', 'North Indian'),
		('SI', 'South Indian'),
		('FF', 'Fast Food'),
		('C', 'Continental'),
		('B', 'Beverage'),
		('D', 'Desset'),]

	category = forms.ChoiceField(choices = type_choices, widget=forms.Select(attrs={'class':'form-control'}), required=True)

class ROrderDetailsForm(forms.Form):
	first_name = forms.CharField(label = 'First Name', max_length = 20, required = False, widget=forms.TextInput(attrs={'class' : 'form-control'}), disabled = True)
	last_name = forms.CharField(label = 'Last Name', max_length = 20, required = False, widget=forms.TextInput(attrs={'class' : 'form-control'}), disabled = True)
	address = forms.CharField(label = 'Address', max_length = 200, required = False, widget=forms.TextInput(attrs={'class' : 'form-control'}), disabled = True)
	contact = forms.CharField(label = 'Contact', max_length = 200, required = False, widget=forms.TextInput(attrs={'class' : 'form-control'}), disabled = True)
	amount = forms.IntegerField(label = 'Bill Amount', required = False, widget=forms.TextInput(attrs={'class' : 'form-control'}), disabled = True)
	type_choices = [
		
		('P', 'Under Preparation'),
		('O', 'Dispatched'),
		('D', 'Delivered'),
		
	]
	status = forms.ChoiceField(choices=type_choices,widget=forms.Select(attrs={'class':'form-control'}))

class CDishForm(forms.Form):
	qty = forms.IntegerField(min_value = 0, label = 'Quantity', widget=forms.TextInput(attrs={'class' : 'form-control'}))


class cartForm(forms.Form):
	temp = 'temp'
<<<<<<< HEAD

class EmptyForm(forms.Form):
	a = 2

=======
>>>>>>> 0d54d2aa73f62f7e47a019180b1383d21757328e
