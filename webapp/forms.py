from django import forms
from django.core.validators import RegexValidator
from .models import *

class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"




class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label="Enter First Name",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                'class': 'form-control'
            }
        )
    )
    last_name = forms.CharField(
        label="Enter Your Last Name",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'class': 'form-control'
            }
        )
    )
    user_name = forms.CharField(
        label="Enter Your USerName",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'UserName',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        validators =[RegexValidator(regex ='^[a-zA-Z0-9@#$%^&*()]*$', code='Invalid_Password')],
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
    )
    mobile = forms.CharField(
        label="Enter Your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Mobile Number',
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email ID",
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email ID',
                'class': 'form-control'
            }
        )
    )


class LoginForm(forms.Form):
    user_name = forms.CharField(
        label="Enter Your USerName",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'User Name',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
    )
