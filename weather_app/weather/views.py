import os
from django.shortcuts import render
from .services import get_weather


def weather(request):
    city = request.GET.get('city', 'London') #hardcoded for now
    api_key = os.environ.get('OPENWEATHERMAP_API_KEY')

    weather_data = get_weather(city, api_key)
    print('goku', weather_data)
    context = {'weather': weather_data, 'city_name': city}
    return render(request, 'weather/weather.html', context)
