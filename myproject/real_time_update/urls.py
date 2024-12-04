from django.urls import path
from . import views

urlpatterns = [
    path("", views.real_time_update, name="real_time_update"),
]
