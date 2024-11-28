from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Transport 
from django.contrib.auth.models import User
from bookings.models import Booking
from django.contrib.contenttypes.models import ContentType

from .forms import  TransportForm

# Create your views here.

def transportlist(request):
    transports = Transport.objects.all()
    context = {'transports':transports}
    return render(request, 'transports/transportlist.html', context)

@login_required
def transportForm(request):
    if request.method == "POST":
        form = TransportForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            transport = form.save(commit=False)
            transport.created_by = request.user
            transport.save()
            return redirect(transportlist)
        else:
            print('invalid form')
    else:
        form = TransportForm()
    return render(request, "transports/transportform.html", {"form": form})

def updatetransport_view(request, id):
    listing = Transport.objects.all().filter(id = id).first()
    if request.method == 'POST':
        form = transportForm(request.POST, instance = listing)
        if form.is_valid():
            form.save()
            return redirect(usertransports_view)
    else:
        form = transportForm(instance=listing)
        return render(request, 'transports/updatetransport.html', {"form":form, "listing": listing})
    
@login_required
def deletetransport_view(request, id):
    listing = Transport.objects.all().filter(id = id).first()
    if request.method == 'POST':
        listing.delete()
        return redirect(usertransports_view)
       
    
@login_required
def usertransports_view(request):
    transports = Transport.objects.filter(created_by = request.user)
    context = {'transports':transports}
    return render(request, 'transports/usertransports.html', context)

@login_required
def transportdetail_view(request, id):
    if request.method == 'POST':
        transport = Transport.objects.get(id = id)
        quantity = int(request.POST.get('quantity'))
        booking = Booking.objects.create(
            user = request.user,
            content_type=ContentType.objects.get_for_model(transport),
            object_id=transport.id,
            status='confirmed',
            quantity = quantity,
            amount = transport.price * quantity
        )
        transport.available_bookings = transport.available_bookings - quantity
        transport.save()
        return redirect('home')

    transports = Transport.objects.filter(id = id)
    context = {'transports':transports}
    return render(request, 'transports/transportdetail.html', context)