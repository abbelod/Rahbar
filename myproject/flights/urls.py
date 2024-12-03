from django.urls import path
from . import views

urlpatterns = [
    path('', views.flightlist, name = "flightlist"),
    path('flightform/', views.flightform, name = "flightform"),
    path('flightlist/', views.flightlist, name = "flightlist"),
    path('userflights/', views.userflights_view, name = "userflights"),
    path('updateflight/<int:id>/', views.updateflight_view, name = "updateflight"),
    path('deleteflight/<int:id>/', views.deleteflight_view, name = "deleteflight"),
    path('flightdetail/<int:id>/', views.flightdetail_view, name = "flightdetail"),
]
