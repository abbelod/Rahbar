from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotellist, name = "hotellist"),
    path('hotelform', views.hotelform, name = "hotelform"),
    path('hotellist/', views.hotellist, name = "hotellist"),
    path('userhotels/', views.userhotels_view, name = "userhotels"),
    path('updatehotel/<int:id>/', views.updatehotel_view, name = "updatehotel"),
    path('deletehotel/<int:id>/', views.deletehotel_view, name = "deletehotel"),
    path('hoteldetail/<int:id>/', views.hoteldetail_view, name = "hoteldetail"),
]
