from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Add_itinerary, name = "planner")
]