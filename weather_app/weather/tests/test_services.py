from django.test import TestCase
from weather.services import get_weather


class TestGetWeather(TestCase):
    def test_get_weather(self):
        city = 'Recife'
        api_key = 'test_key'

        # Act
        result = get_weather(city, api_key)

        # Assert
        self.assertEqual(result['cod'], 200)
        self.assertEqual(result['name'], city)

    def test_get_weather_with_invalid_city(self):
        city = 'invalid_city'
        api_key = 'test_key'

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
        self.assertEqual(
            result['message'], 'Invalid API key. Please see http://openweathermap.org/faq#error401 for more info.')
