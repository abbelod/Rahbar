from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings_view, name = "bookings"),
    path('cancelbooking/<int:id>/', views.cancelbooking_view, name = "cancelbooking"),
]
  



