from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Hotel 
from django.contrib.auth.models import User
from bookings.models import Booking
from django.contrib.contenttypes.models import ContentType
from .forms import HotelForm
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(["GET", "POST"])  # Sensitive
def hotellist(request):
    hotels = Hotel.objects.all()
    context = {'hotels':hotels}
    return render(request, 'hotels/hotellist.html', context)

@login_required
@require_http_methods(["GET", "POST"])  # Sensitive
def hotelform(request):
    if request.method == "POST":
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            hotel = form.save(commit = False)
            hotel.created_by = request.user
            hotel.save()
            return redirect(hotellist)
        else:
            print('invalid form')
    else:
        form = HotelForm()
    return render(request, "hotels/hotelform.html", {"form": form})

@require_http_methods(["GET", "POST"])  # Sensitive
def updatehotel_view(request, id):
    listing = Hotel.objects.all().filter(id = id).first()
    if request.method == 'POST':
        form = HotelForm(request.POST, instance = listing)
        if form.is_valid():
            form.save()
            return redirect('listings')
    else:
        form = HotelForm(instance=listing)
        return render(request, 'hotels/updatehotel.html', {"form":form, "listing": listing})
 
@login_required
@require_http_methods(["GET", "POST"])  # Sensitive
def deletehotel_view(request, id):
    listing = Hotel.objects.all().filter(id = id).first()
    if request.method == 'POST':
        listing.delete()
        return redirect('listings')
       
@require_http_methods(["GET", "POST"])  # Sensitive  
@login_required
def userhotels_view(request):
    hotels = Hotel.objects.filter(created_by = request.user)
    print(hotels)
    context = {'hotels':hotels}
    return render(request, 'hotels/userhotels.html', context)

@login_required
@require_http_methods(["GET", "POST"])  # Sensitive
def hoteldetail_view(request, id):
    if request.method == 'POST':
        hotel = Hotel.objects.get(id = id)
        quantity = int(request.POST.get('quantity'))
        Booking.objects.create(
            user = request.user,
            content_type=ContentType.objects.get_for_model(hotel),
            object_id=hotel.id,
            status='confirmed',
            quantity = quantity,
            amount = hotel.price_per_night * quantity
        )
        hotel.available_bookings = hotel.available_bookings - quantity
        hotel.save()
        return redirect('home')

    hotels = Hotel.objects.filter(id = id)
    context = {'hotels':hotels}
    return render(request, 'hotels/hoteldetail.html', context)