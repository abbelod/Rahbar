from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
# Create your views here.
@require_http_methods(["GET", "POST"])  # Sensitive
def home(request):
    profile = None
    if request.user.is_authenticated:
        profile = request.user.profile

    return render(request, 'home/index.html', {"profile": profile})

