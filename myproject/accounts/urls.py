from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name = "login"),
    path('signup/', views.register_view, name = "signup"),
    path('logout/', views.logout_view, name = "logout"),
    path('listings/', views.listings, name = "listings"),
    path('createlistings/', views.createlistings_view, name = "createlistings"),
]
