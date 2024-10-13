import requests
from bs4 import BeautifulSoup

# Constants
CITY = 'Oulu'
BASE_URL = f'https://www.weather-forecast.com/locations/{CITY}/forecasts/latest'

def get_weather(city):
    # Send GET request
    response = requests.get(BASE_URL)
    response.raise_for_status()  # Check if the request was successful

    # Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract weather information
    weather_info = soup.find('span', class_='phrase').text

    return weather_info

if __name__ == '__main__':
    try:
        weather = get_weather(CITY)
        print(f"Weather in {CITY}: {weather}")
    except Exception as e:
        print(f"An error occurred: {e}")