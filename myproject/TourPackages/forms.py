from typing import Any
from django import forms
from .models import Tour
from django.contrib.auth.models import User

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['name', 'origin_country', 'destination_country', 'number_of_nights', 'price', 'image', 'available_bookings','description']
    
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    password_confirm = forms.CharField(widget = forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

