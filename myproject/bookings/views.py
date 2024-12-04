from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Booking
from django.views.decorators.http import require_http_methods


# Create your views here.

@login_required
@require_http_methods(["GET"])  # Sensitive
def bookings_view(request):
    bookings = request.user.bookings.all()
    print(bookings)
    return render(request, 'bookings/bookings.html', {"bookings": bookings})

@login_required
@require_http_methods(["POST"])  # Sensitive
def cancelbooking_view(request, id):
    if request.method == 'POST':
        booking = Booking.objects.get(id = id)
        booking.status = 'Cancelled'
        listing = booking.listing
        listing.available_bookings = listing.available_bookings + booking.quantity
        listing.save()
        booking.save()
        return redirect('bookings')