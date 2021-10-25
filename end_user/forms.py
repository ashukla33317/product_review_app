from django import forms
from django.forms.widgets import PasswordInput


class LoginForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput())

class SignUpForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput())
    email=forms.EmailField()
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    