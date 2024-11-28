from django.db import models
from django.contrib.auth.models import User

class Transport(models.Model):
    TRANSPORT_TYPES = (
        ('bus', 'Bus'),
        ('train', 'Train'),
        ('taxi', 'Taxi'),
        ('rental', 'Rental Vehicle'),
        ('other', 'Other'),
    )
    name = models.CharField(max_length=100, help_text="Name of the transport service.")
    transport_type = models.CharField(max_length=20, choices=TRANSPORT_TYPES, help_text="Type of transport.")
    capacity = models.PositiveIntegerField(help_text="Total passenger capacity.")
    route = models.CharField(max_length=200, help_text="Route details (e.g., City A to City B).")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per ticket or rental.")
    available_bookings = models.PositiveIntegerField(default=0, help_text="Number of seats currently available.")
    image = models.ImageField(upload_to='transport/images', blank=True, help_text="Optional image of the transport service.")
    description = models.TextField(max_length=500, blank=True, help_text="Additional information about the transport service.")
   
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transport_listings", help_text="User who created this listing.")

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True, help_text="When the listing was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="When the listing was last updated.")

    def __str__(self):
        return f"{self.name} - {self.transport_type}"

    class Meta:
        verbose_name = "Transport Listing"
        verbose_name_plural = "Transport Listings"