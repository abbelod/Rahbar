from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = [
            'name',
            'airline',
            'origin',
            'destination',
            'departure_time',
            'arrival_time',
            'duration',
            'price',
            'available_bookings',
            'image',
            'description',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add flight details'}),
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'arrival_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
        }
