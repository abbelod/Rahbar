from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Flight 
from django.contrib.auth.models import User
from bookings.models import Booking
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.http import require_http_methods

from .forms import FlightForm
# Create your views here.

@require_http_methods(["GET"])  # Sensitive
def flightlist(request):
    flights = Flight.objects.all()
    context = {'flights':flights}
    return render(request, 'flights/flightlist.html', context)

@login_required
@require_http_methods(["GET", "POST"])  # Sensitive
def flightform(request):
    if request.method == "POST":
        form = FlightForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            flight = form.save(commit = False)
            flight.created_by = request.user
            flight.save()
            return redirect(flightlist)
        else:
            print('invalid form')
    else:
        form = FlightForm()
    return render(request, "flights/flightform.html", {"form": form})

@require_http_methods(["GET", "POST"])  # Sensitive
def updateflight_view(request, id):
    listing = Flight.objects.all().filter(id = id).first()
    if request.method == 'POST':
        form = FlightForm(request.POST, instance = listing)
        if form.is_valid():
            form.save()
            return redirect(userflights_view)
    else:
        form = FlightForm(instance=listing)
        return render(request, 'flights/updateflight.html', {"form":form, "listing": listing})
    
@login_required
@require_http_methods(["GET", "POST"])  # Sensitive
def deleteflight_view(request, id):
    listing = Flight.objects.all().filter(id = id).first()
    if request.method == 'POST':
        listing.delete()
        return redirect(userflights_view)
       
    
@login_required
@require_http_methods(["GET", "POST"])  # Sensitive
def userflights_view(request):
    flights = Flight.objects.filter(created_by = request.user)
    print(flights)
    context = {'flights':flights}
    return render(request, 'flights/userflights.html', context)

@login_required
@require_http_methods(["GET", "POST"])  # Sensitive
def flightdetail_view(request, id):
    if request.method == 'POST':
        flight = Flight.objects.get(id = id)
        quantity = int(request.POST.get('quantity'))
        Booking.objects.create(
            user = request.user,
            content_type=ContentType.objects.get_for_model(flight),
            object_id=flight.id,
            status='confirmed',
            quantity = quantity,
            amount = flight.price * quantity
        )
        flight.available_bookings = flight.available_bookings - quantity
        flight.save()
        return redirect('home')

    flights = Flight.objects.filter(id = id)
    context = {'flights':flights}
    return render(request, 'flights/flightdetail.html', context)