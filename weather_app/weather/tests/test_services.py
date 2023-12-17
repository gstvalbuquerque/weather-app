from django.test import TestCase
from weather.services import get_weather
import os



class TestGetWeather(TestCase):

    def test_get_weather(self):
        city = 'Recife'
        api_key = os.environ.get('OPENWEATHERMAP_API_KEY')

        # Act
        result = get_weather(city, api_key)

        # Assert
        self.assertEqual(result["city"], city)

    def test_get_weather_with_invalid_city(self):
        city = 'invalid_city'
        api_key = os.environ.get('OPENWEATHERMAP_API_KEY')

        # Act
        result = get_weather(city, api_key)

        # Assert
        self.assertEqual(result['cod'], '404')
        self.assertEqual(result['message'], 'city not found')

    def test_get_weather_with_invalid_api_key(self):
        city = 'Recife'
        api_key = 'invalid_key'

        # Act
        result = get_weather(city, api_key)

        # Assert
        self.assertEqual(result['cod'], 401)
