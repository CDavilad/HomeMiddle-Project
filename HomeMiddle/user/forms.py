from django import forms
from .models import *
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ["address", "creditcard"]


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
