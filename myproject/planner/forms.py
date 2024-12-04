from django import forms
from .models import Itinerary, Attraction, TravelRoute

class ItineraryForm(forms.ModelForm):
    class Meta:
        model = Itinerary
        fields = ['name', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'Select Start Date'
                }
            ),
            'end_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'Select End Date'
                }
            ),
        }
class AttractionForm(forms.ModelForm):
    class Meta:
        model = Attraction
        fields = ['name', 'description', 'location', 'start_time', 'end_time']

class TravelRouteForm(forms.ModelForm):
    class Meta:
        model = TravelRoute
        fields = ['start_location', 'end_location', 'travel_mode', 'departure_time', 'arrival_time']
