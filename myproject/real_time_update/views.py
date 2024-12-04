import requests
from django.conf import settings
from django.shortcuts import render


def get_geocode(address):
    """
    Fetch geocode (latitude/longitude) for an address using the Google Maps API.
    """
    url = f"https://{settings.GOOGLE_MAPS_HOST}/maps/api/geocode/json"
    headers = {
        "x-rapidapi-key": settings.RAPIDAPI_KEY,
        "x-rapidapi-host": settings.GOOGLE_MAPS_HOST,
    }
    params = {
        "address": address,
        "language": "en",
        "region": "en",
        "result_type": "administrative_area_level_1",
        "location_type": "APPROXIMATE",
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            location = data["results"][0]["geometry"]["location"]
            return {"latitude": location["lat"], "longitude": location["lng"]}
    return None


def get_weather(city):
    """
    Fetch weather data for a city using the OpenWeatherMap API.
    """
    url = f"https://{settings.OPEN_WEATHER_HOST}/city/{city}/EN"
    headers = {
        "x-rapidapi-key": settings.RAPIDAPI_KEY,
        "x-rapidapi-host": settings.OPEN_WEATHER_HOST,
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if "data" in data:
            return {
                "city": city,
                "temperature": data["data"]["temperature"],
                "description": data["data"]["description"],
            }
    return None


def real_time_update(request):
    """
    Combine geocode and weather data into a single view.
    """
    address = request.GET.get("address", "1600 Amphitheatre Parkway, Mountain View, CA")
    city = request.GET.get("city", "London")

    geocode_data = get_geocode(address)
    weather_data = get_weather(city)

    return render(request, "real_time_update/weather_map.html", {
        "geocode": geocode_data,
        "weather": weather_data,
    })
