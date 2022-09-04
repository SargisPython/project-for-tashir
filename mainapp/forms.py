from django import forms
from django.forms import Textarea, TextInput, Select, SelectMultiple, FileInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'placeholder':'Your username','class': 'form-control'}))
    forname=forms.CharField(label="Forname",widget=forms.TextInput(attrs={'placeholder':'Your forname','class':'form-control'}))
    lastname=forms.CharField(label="Lastname",widget=forms.TextInput(attrs={'placeholder':'Your lastname','class':'form-control'}))
    email=forms.EmailField(required=True,label="Email",widget=forms.TextInput(attrs={'placeholder':'Your email','class':'form-control'}))
    phone=forms.CharField(required=True,label="Phone",widget=forms.NumberInput(attrs={'placeholder':'Your phone','class':'form-control'}))
    password1=forms.CharField(label="Password",help_text="grel arnvazy 3 nish 3 tar ",widget=forms.PasswordInput(attrs={'placeholder':'Your password','class':'form-control'}) )
    password2=forms.CharField(label="Password",help_text="krknel password ",widget=forms.PasswordInput(attrs={'placeholder':'Your password','class':'form-control'}) )

    class Meta:
        model=User
        fields=("username","forname","lastname","email","phone","password1",'password2')



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder':'Your Username','class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Your Password','class': 'form--control'}))



class UserAdd_contactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','people','date','number']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control' }),
            'people': Textarea(attrs={'class': 'form-control'}),
            'date': Textarea(attrs={'class': 'form-control',}),
            'number': Textarea(attrs={'class': 'form-control', }),
        }