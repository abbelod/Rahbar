from django.shortcuts import render, HttpResponse

# Create your views here.

def planner(request):
    return render(request, 'itinerary.html')