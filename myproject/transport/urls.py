from django.urls import path
from . import views

urlpatterns = [
    path('', views.transportlist, name = "transportlist"),
    path('transportform', views.transportForm, name = "transportform"),
    path('transportlist/', views.transportlist, name = "transportlist"),
    path('usertransports/', views.usertransports_view, name = "usertransports"),
    path('updatetransport/<int:id>/', views.updatetransport_view, name = "updatetransport"),
    path('deletetransport/<int:id>/', views.deletetransport_view, name = "deletetransport"),
    path('transportdetail/<int:id>/', views.transportdetail_view, name = "transportdetail"),
]
