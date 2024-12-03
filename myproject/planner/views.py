from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_http_methods
# Create your views here.

@require_http_methods(["GET", "POST"])  # Sensitive
def add_itinerary(request):
    return render(request, 'itinerary.html')