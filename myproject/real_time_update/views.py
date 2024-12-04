import requests
from django.conf import settings
from django.shortcuts import render
from urllib.parse import quote

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
    # city = urllib.parse.urlencode(city)
    # url = f"https://{settings.OPEN_WEATHER_HOST}/city/{city}/EN"
    # headers = {
    #     "x-rapidapi-key": settings.RAPIDAPI_KEY,
    #     "x-rapidapi-host": settings.OPEN_WEATHER_HOST,
    # }
    # response = requests.get(url, headers=headers)
    # if response.status_code == 200:
    #     data = response.json()
    #     if "data" in data:
    #         return {
    #             "city": city,
    #             "temperature": data["data"]["temperature"],
    #             "description": data["data"]["description"],
    #         }
          
    # return{
    #              "city": 'lahore',
    #             "temperature": "15",
    #             "description": 'Sunny',
    #         }
    lat, long = get_lat_lon(city)
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}8&longitude={long}&current=temperature_2m,weather_code&timezone=auto&forecast_days=1'
    response = requests.get(url)
    if response.status_code == 200:
            data = response.json()
            if "data" in data:
                return {
                    "city": city,
                    "temperature": data["data"]["current"]["temperature_2m"],
                    "description": data["data"]['current']["weather_code"],
                }
            
    return{
                 "city": 'lahore',
                "temperature": "15",
                "description": 'Sunny',
            }

def real_time_update(request):
    """
    Combine geocode and weather data into a single view.
    """
    address = request.GET.get("address", "1600 Amphitheatre Parkway, Mountain View, CA")
    city = request.GET.get("city", "London")

    geocode_data = get_geocode(address)
    weather_data = get_weather(city)
    print(weather_data)

    return render(request, "real_time_update/weather_map.html", {
        "geocode": geocode_data,
        "weather": weather_data,
    })


def get_lat_lon(city):
    city = quote(city)
    url = f'https://api.opencagedata.com/geocode/v1/json?q={city}&key={settings.GEOCODING_API}'
    response = requests.get(url)
    print(response.json())
    # lat= response.json()['data']['results']['geometry']['lat']
    # long= response.json()['data']['results']['geometry']['lng']
    return 1, 2
