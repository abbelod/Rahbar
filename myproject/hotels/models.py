from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)  # City or area
    description = models.TextField()  # Detailed description of the hotel
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)  # Cost per night
    image = models.ImageField(upload_to='images/hotel_images/', blank=True, default='default_hotel.png')  # Hotel image
    amenities = models.TextField(blank=True, help_text="Comma-separated list of amenities")  # e.g., Wi-Fi, Pool
    available_bookings = models.PositiveIntegerField(default=0)  # Number of rooms available
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hotel_listings')  # Associated company user
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update

    def __str__(self):
        return self.name
