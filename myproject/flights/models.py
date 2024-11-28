from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    name = models.CharField(max_length=100)  # Name of the flight
    airline = models.CharField(max_length=100)  # Airline operating the flight
    origin = models.CharField(max_length=100)  # Origin city/airport
    destination = models.CharField(max_length=100)  # Destination city/airport
    departure_time = models.DateTimeField()  # Departure time
    arrival_time = models.DateTimeField()  # Arrival time
    duration = models.CharField(max_length=20)  # Duration of the flight
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Ticket price
    available_bookings = models.PositiveIntegerField()  # Number of available seats
    image = models.ImageField(upload_to='images/flight_images/', blank=True, null=True, default='default_flight.png')  # Optional flight image
    description = models.TextField(max_length=500, blank=True)  # Description (optional)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='flight_listings'
    )  # Creator of the flight listing

    def __str__(self):
        return f"{self.name} ({self.airline}) - {self.origin} to {self.destination}"
