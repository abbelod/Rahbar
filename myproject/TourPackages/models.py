from django.db import models

# Create your models here.
class Tour(models.Model):
    name = models.CharField(max_length=20)
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images', default='def.png', blank=True)
    available_bookings = models.IntegerField(default=10)
    description = models.CharField(max_length=500)

    def __str__(self):
        return (f"ID:{self.id}: FROM: {self.origin_country} TO: {self.destination_country} Number of Nights: {self.number_of_nights} Price :{self.price}")