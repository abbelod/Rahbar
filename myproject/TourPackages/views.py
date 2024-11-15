from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tour 
from .forms import  TourForm

# Create your views here.

def tourlist(request):
    tours = Tour.objects.all()
    context = {'tours':tours}
    return render(request, 'tours/tourlist.html', context)


def tourForm(request):
    if request.method == "POST":
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(tourlist)
    
    else:
        form = TourForm()
    return render(request, "tours/tourform.html", {"form": form})


    