"""Exercise 3: Current Weather In City or Country using Open-Meteo API"""

from api_client import get_current_weather


def main():
    location = input("Enter a city or country name: ")

    data = get_current_weather(location)
    if data is None:
        print("City or country not found.")
        return

    # Accessing the current weather data from the API response
    current = data["current_weather"]

    print(f"Current Weather in {location}:")

    # API returns temperature in Celsius
    print(f"Temperature: {current['temperature']}°C")

    # API returns windspeed in km/h
    print(f"Windspeed: {current['windspeed']} km/h")

    # API returns wind direction in degrees
    print(f"Wind Direction: {current['winddirection']}°")


if __name__ == "__main__":
    main()

# ? Example usage:
# Enter a city or country name: London
# Current Weather in London:
# Temperature: 5.2°C
# Windspeed: 20.8 km/h
# Wind Direction: 104°

# Enter a city or country name: Australia
# Current Weather in Australia:
# Temperature: 28.1°C
# Windspeed: 20.3 km/h
# Wind Direction: 160°

# Enter a city or country name: ErrorCity
# City or country not found.
