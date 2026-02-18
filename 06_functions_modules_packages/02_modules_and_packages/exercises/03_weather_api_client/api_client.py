"""Exercise 3: Current Weather API Client module"""

import requests


def get_current_weather(location):
    """Fetches the current weather for a given city or country using the Open-Meteo API."""
    # ? Step 1: Convert city name to coordinates
    # Open-Meteo's geocoding API endpoint
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    # Parameters for the geocoding API request:
    geo_params = {
        "name": location,
        "count": 1  # Only the top result to get the coordinates
    }

    # Send a GET request to the geocoding API
    geo_response = requests.get(geo_url, params=geo_params, timeout=10)

    # Check if the geocoding request was successful
    geo_response.raise_for_status()

    # Parse the JSON response to extract latitude and longitude
    geo_data = geo_response.json()

    if "results" not in geo_data:
        return None

    # Get the first result (most relevant)
    location_data = geo_data["results"][0]

    # Extract latitude from the geocoding response
    latitude = location_data["latitude"]

    # Extract longitude from the geocoding response
    longitude = location_data["longitude"]

    # ? Step 2: Fetch current weather
    # Open-Meteo's weather API endpoint
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }

    # Send a GET request to the weather API to fetch current weather data
    weather_response = requests.get(
        weather_url, params=weather_params, timeout=10)
    # Timeout set to 10 seconds to prevent hanging if the API is slow to respond

    # Check if the weather request was successful
    weather_response.raise_for_status()

    # Return the JSON response containing current weather data
    return weather_response.json()
