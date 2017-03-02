from .models import CustomUser
from django.contrib.auth.models import User
from django import forms

class CustomerForm(forms.ModelForm):
    password = forms.CharField(required = True,widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    username = forms.CharField(required = True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    first_name = forms.CharField(required = True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(required = True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    contact = forms.CharField(required = True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    address = forms.CharField(required = True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(required = True,widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password' ,'first_name','last_name', 'contact','address')

class RestForm(forms.ModelForm):
    password = forms.CharField(required = True,widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    username = forms.CharField(required = True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    first_name = forms.CharField( label="Name of Restaurant" ,required = True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    # last_name = forms.CharField(required = True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    contact = forms.CharField(required = True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    address = forms.CharField(required = True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(required = True,widget=forms.EmailInput(attrs={'class' : 'form-control'}))

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
	when = forms.DateTimeField(label = 'Date Time of Order', required = False, disabled = True)
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

class EmptyForm(forms.Form):
	a = 2


class CeditForm(forms.ModelForm):
    # password = forms.CharField(min_length = 1, widget=forms.PasswordInput())
    # username = forms.CharField(disabled=True)
    password = forms.CharField(min_length = 1,widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    username = forms.CharField(disabled=True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'})) 
    class Meta:
        model = CustomUser
        fields = ('username','email', 'password' ,'first_name','last_name', 'contact','address')


class ReditForm(forms.ModelForm):
    # password = forms.CharField(min_length = 1,widget=forms.PasswordInput())
    # first_name = forms.CharField(label = 'Name of restaurant', max_length = 20, required = True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    username = forms.CharField(disabled=True)
    password = forms.CharField(min_length = 1,widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    username = forms.CharField(disabled=True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    first_name = forms.CharField( label="Name of Restaurant" ,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'})) 
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'first_name', 'contact', 'address')