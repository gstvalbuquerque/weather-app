import requests


def get_weather(city, api_key):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
