from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')  # User who made the booking
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Type of the listing (Tour, Hotel, etc.)
    object_id = models.PositiveIntegerField()  # ID of the specific listing
    listing = GenericForeignKey('content_type', 'object_id')  # Generic relation to the listing
    booking_date = models.DateTimeField(auto_now_add=True)  # When the booking was made
    quantity = models.PositiveIntegerField(default=1)
    amount = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=(
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('cancelled', 'Cancelled'),
        ),
        default='pending'
    )

    def __str__(self):
        return f"Booking by {self.user.username} for {self.listing}"

