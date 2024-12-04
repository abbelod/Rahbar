from django.db import models
from django.contrib.auth.models import User

class Itinerary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Attraction(models.Model):
    itinerary = models.ForeignKey(Itinerary, related_name='attractions', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name

class TravelRoute(models.Model):
    itinerary = models.ForeignKey(Itinerary, related_name='routes', on_delete=models.CASCADE)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    travel_mode = models.CharField(max_length=100)  # e.g., Car, Train, Flight, etc.
    departure_time = models.TimeField()
    arrival_time = models.TimeField()

    def __str__(self):
        return f"{self.start_location} to {self.end_location}"
