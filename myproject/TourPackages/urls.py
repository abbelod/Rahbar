from django.urls import path
from . import views

urlpatterns = [
    path('', views.tourlist, name = "tourlist"),
    path('tourform', views.tourForm, name = "tourform"),
]
