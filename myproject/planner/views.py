from django.shortcuts import render, HttpResponse

# Create your views here.

def Add_itinerary(request):
    return render(request, 'itinerary.html')