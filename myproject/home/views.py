from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    profile = None
    if request.user.is_authenticated:
        profile = request.user.profile

    return render(request, 'home/index.html', {"profile": profile})

