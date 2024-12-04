from django.shortcuts import render, redirect
from .forms import ItineraryForm, AttractionForm, TravelRouteForm
from .models import Itinerary, Attraction, TravelRoute

def create_itinerary(request):
    if request.method == 'POST':
        itinerary_form = ItineraryForm(request.POST)
        if itinerary_form.is_valid():
            itinerary = itinerary_form.save(commit=False)
            itinerary.user = request.user
            itinerary.save()
            return redirect('add_attractions', itinerary_id=itinerary.id)
    else:
        itinerary_form = ItineraryForm()
    return render(request, 'planner/create_itinerary.html', {'itinerary_form': itinerary_form})

def add_attractions(request, itinerary_id):
    itinerary = Itinerary.objects.get(id=itinerary_id)
    if request.method == 'POST':
        attraction_form = AttractionForm(request.POST)
        if attraction_form.is_valid():
            attraction = attraction_form.save(commit=False)
            attraction.itinerary = itinerary
            attraction.save()
            return redirect('add_routes', itinerary_id=itinerary.id)
    else:
        attraction_form = AttractionForm()
    return render(request, 'planner/add_attractions.html', {'itinerary': itinerary, 'attraction_form': attraction_form})

def add_routes(request, itinerary_id):
    itinerary = Itinerary.objects.get(id=itinerary_id)
    if request.method == 'POST':
        route_form = TravelRouteForm(request.POST)
        if route_form.is_valid():
            route = route_form.save(commit=False)
            route.itinerary = itinerary
            route.save()
            return redirect('view_itinerary', itinerary_id=itinerary.id)
    else:
        route_form = TravelRouteForm()
    return render(request, 'planner/add_routes.html', {'itinerary': itinerary, 'route_form': route_form})

def view_itinerary(request, itinerary_id):
    itinerary = Itinerary.objects.get(id=itinerary_id)
    attractions = itinerary.attractions.all()
    routes = itinerary.routes.all()
    return render(request, 'planner/view_itinerary.html', {'itinerary': itinerary, 'attractions': attractions, 'routes': routes})
