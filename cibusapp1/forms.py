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
        fields = ('username', 'email', 'password', 'first_name')