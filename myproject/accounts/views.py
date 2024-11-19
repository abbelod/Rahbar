from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import login_requiredMixin
from django.views import View
from django.contrib.auth.models import User
from .forms import RegisterForm, ProfileForm
from TourPackages.models import Tour
from bookings.models import Booking



# Create your views here.
def register_view(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
        profile_form = ProfileForm()

    context={"form":form , "profile_form":profile_form}
    return render(request, 'account/signup.html', context)


def login_view(request):
    
    error_message=" "
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid Credentials"

    return render(request, 'account/login.html', {"error":error_message})



def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('home')

@login_required
def user_dashboard_view(request):
    return render(request, 'account/userdashboard.html')

@login_required
def listings(request):
    tours = request.user.tours.all()
    
    print(tours)
    return render (request, 'account/listings.html', {"tours":tours})

@login_required
def createlistings_view(request):
    return render (request, 'account/createlistings.html')

@login_required
def bookings_view(request):
    bookings = request.user.bookings.all()
    print(bookings)
    return render(request, 'account/bookings.html', {"bookings": bookings})
