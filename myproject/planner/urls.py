from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_itinerary, name='create_itinerary'),
    path('add_attractions/<int:itinerary_id>/', views.add_attractions, name='add_attractions'),
    path('add_routes/<int:itinerary_id>/', views.add_routes, name='add_routes'),
    path('view_itinerary/<int:itinerary_id>/', views.view_itinerary, name='view_itinerary'),
]
