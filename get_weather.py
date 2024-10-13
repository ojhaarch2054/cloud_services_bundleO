"""
This module fetches and displays the weather information for a specified city.
"""

import requests
from bs4 import BeautifulSoup

# Constants
CITY = 'Oulu'
BASE_URL = f'https://www.weather-forecast.com/locations/{CITY}/forecasts/latest'

def get_weather():
    """
    Fetches the weather information for the specified city.

    Returns:
        str: The weather information.
    """
    # Send GET request with timeout
    response = requests.get(BASE_URL, timeout=10)
    response.raise_for_status()  # Check if the request was successful

    # Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract weather information
    weather_info = soup.find('span', class_='phrase').text

    return weather_info

if __name__ == '__main__':
    try:
        weather = get_weather()
        print(f"Weather in {CITY}: {weather}")
    except requests.RequestException as e:
        print(f"An error occurred with the request: {e}")
    except (requests.Timeout, requests.ConnectionError) as e:
        print(f"A network error occurred: {e}")
