from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Tour 
from django.contrib.auth.models import User
from bookings.models import Booking
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.http import require_http_methods
from .forms import  TourForm

# Create your views here.
@require_http_methods(["GET", "POST"])  # Sensitive
def tourlist(request):
    tours = Tour.objects.all()
    context = {'tours':tours}
    return render(request, 'tours/tourlist.html', context)
@require_http_methods(["GET", "POST"])  # Sensitive
@login_required
def tourForm(request):
    if request.method == "POST":
        form = TourForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.created_by = request.user
            form.save()
            return redirect(tourlist)
        else:
            print('invalid form')
    else:
        form = TourForm()
    return render(request, "tours/tourform.html", {"form": form})
@require_http_methods(["GET", "POST"])  # Sensitive
def updatetour_view(request, id):
    listing = Tour.objects.all().filter(id = id).first()
    if request.method == 'POST':
        form = TourForm(request.POST, instance = listing)
        if form.is_valid():
            form.save()
            return redirect(usertours_view)
    else:
        form = TourForm(instance=listing)
        return render(request, 'tours/updatetour.html', {"form":form, "listing": listing})
@require_http_methods(["GET", "POST"])  # Sensitive   
@login_required
def deletetour_view(request, id):
    listing = Tour.objects.all().filter(id = id).first()
    if request.method == 'POST':
        listing.delete()
        return redirect(usertours_view)
       
    
@login_required
@require_http_methods(["GET", "POST"])  # Sensitive
def usertours_view(request):
    tours = Tour.objects.filter(created_by = request.user)
    print(tours)
    context = {'tours':tours}
    return render(request, 'tours/usertours.html', context)

@login_required
@require_http_methods(["GET", "POST"])  # Sensitive
def tourdetail_view(request, id):
    if request.method == 'POST':
        tour = Tour.objects.get(id = id)
        quantity = int(request.POST.get('quantity'))
        booking = Booking.objects.create(
            user = request.user,
            content_type=ContentType.objects.get_for_model(tour),
            object_id=tour.id,
            status='confirmed',
            quantity = quantity,
            amount = tour.price * quantity
        )
        tour.available_bookings = tour.available_bookings - quantity
        tour.save()
        return redirect('home')

    tours = Tour.objects.filter(id = id)
    context = {'tours':tours}
    return render(request, 'tours/tourdetail.html', context)