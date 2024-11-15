from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Tour 
from django.contrib.auth.models import User

from .forms import  TourForm

# Create your views here.

def tourlist(request):
    tours = Tour.objects.all()
    print(tours)
    context = {'tours':tours}
    return render(request, 'tours/tourlist.html', context)

@login_required
def tourForm(request):
    if request.method == "POST":
        form = TourForm(request.POST)
        if form.is_valid():
            form.created_by = request.user
            form.save()
            return redirect(tourlist)
    
    else:
        form = TourForm()
    return render(request, "tours/tourform.html", {"form": form})

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
    
@login_required
def deletetour_view(request, id):
    listing = Tour.objects.all().filter(id = id).first()
    if request.method == 'POST':
        listing.delete()
        return redirect(usertours_view)
       
    
@login_required
def usertours_view(request):
    tours = Tour.objects.filter(created_by = request.user)
    print(tours)
    context = {'tours':tours}
    return render(request, 'tours/usertours.html', context)

