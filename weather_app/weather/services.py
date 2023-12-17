import requests


def get_weather(city, api_key):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
    }

    response = requests.get(url, params=params)
    if response.status_code == requests.codes.ok:
        data = response.json()
        weather = {
            "city": data['name'],
            "temperature": data['main']['temp'],
            "description": data['weather'][0]['description'],
            "icon": data['weather'][0]['icon']
        }
        return weather
    return response.json()
