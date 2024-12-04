import requests
from django.conf import settings
from django.shortcuts import render
from urllib.parse import quote
from .wmo_weather_codes import WMO_WEATHER_CODES



def get_weather_description(weather_code):
    return WMO_WEATHER_CODES.get(weather_code, "Unknown weather condition")

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
    
    cord_data = get_lat_lon(city)
    lat = cord_data['lat']
    long = cord_data["lon"]
    city = cord_data["city"]
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}8&longitude={long}&current=temperature_2m,weather_code&timezone=auto&forecast_days=1'
    response = requests.get(url)
    if response.status_code == 200:
            data = response.json()
            description = get_weather_description(data['current']["weather_code"])
            return {
                "city":city,
                "temperature": data["current"]["temperature_2m"],
                "description": description,
            }
        
    return{
                 "city": 'lahore',
                "temperature": "15",
                "description": 'Sunny',
            }

def real_time_update(request):

    address = request.GET.get("address", "1600 Amphitheatre Parkway, Mountain View, CA")
    city = request.GET.get("city", "London")

    geocode_data = get_geocode(address)
    weather_data = get_weather(city)

    return render(request, "real_time_update/weather_map.html", {
        "geocode": geocode_data,
        "weather": weather_data,
    })


def get_lat_lon(city):
    if not city:
        city = 'London'
    
    city = quote(city)
    url = f'https://api.opencagedata.com/geocode/v1/json?q={city}&key={settings.GEOCODING_API}'
    response = requests.get(url)
    data = response.json()
    if data.get("results"):  # Check if results exist
        first_result = data["results"][0]  # Access the first result
        lat = first_result["geometry"]["lat"]
        lon = first_result["geometry"]["lng"]
        normalized_city = first_result['components']['_normalized_city']
        return {'lat': lat,
                'lon': lon,
                'city': normalized_city
                }
    else:
        print("No results found!")
        return 1, 1

