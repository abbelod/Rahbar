from typing import Any
from django import forms
from .models import Hotel
from django.contrib.auth.models import User

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = [
            'name',
            'location',
            'description',
            'price_per_night',
            'image',
            'amenities',
            'available_bookings',
        ]
    