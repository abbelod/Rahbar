
from django import forms
from .models import Transport
from django.contrib.auth.models import User

class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = [
    'name',                # Name of the transport service
    'transport_type',      # Type of transport (e.g., Bus, Train, etc.)
    'capacity',            # Maximum passenger capacity
    'route',               # Route details (origin to destination)
    'price',    # Ticket or rental price
    'available_bookings',     # Number of currently available seats
    'image',               # Optional image upload
    'description',         # Additional description of the transport
]   
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a short description...'}),
            'route': forms.TextInput(attrs={'placeholder': 'E.g., City A to City B'}),
            'price': forms.NumberInput(attrs={'min': 0, 'step': 0.01}),
            'capacity': forms.NumberInput(attrs={'min': 1}),
            'available_bookings': forms.NumberInput(attrs={'min': 0}),
        }