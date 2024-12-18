from django.urls import path
from . import views

urlpatterns = [
    path('', views.tourlist, name = "tourlist"),
    path('tourform', views.tourform, name = "tourform"),
    path('tourlist/', views.tourlist, name = "tourlist"),
    path('usertours/', views.usertours_view, name = "usertours"),
    path('updatetour/<int:id>/', views.updatetour_view, name = "updatetour"),
    path('deletetour/<int:id>/', views.deletetour_view, name = "deletetour"),
    path('tourdetail/<int:id>/', views.tourdetail_view, name = "tourdetail"),
]
