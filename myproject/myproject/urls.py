"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('/home/')),   #lambda se ham redirect request daal kar direct apny home page [pe ja sakty hain]
    path('admin/', admin.site.urls),
    path('tours/', include('TourPackages.urls')),
    path('hotels/', include('hotels.urls')),
    path('home/', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('planner/', include('planner.urls')),
    path('bookings/', include('bookings.urls')),
    path('transport/', include('transport.urls')),
    path('flights/', include('flights.urls')),
    path('blogs/', include('blog.urls')),
    path('chatbot/', include('chatbot.urls')),
     path('real_time_update/', include('real_time_update.urls')),

]
    
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)