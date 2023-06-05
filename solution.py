import requests
import json

# Using the openWeatherMap API key
API_KEY = "2b09a6bf60997d447ff86f8281a792d9"

def fetch_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        weather_data = json.loads(response.text)
        return weather_data
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
        return None

def parse_weather(weather_data):
    if weather_data is not None:
        weather_main = weather_data["weather"][0]["main"]
        weather_desc = weather_data["weather"][0]["description"]
        temp = weather_data["main"]["temp"]
        temp_celsius = round(temp - 273.15, 2)  # Convert temperature to Celsius
        humidity = weather_data["main"]["humidity"]
        return weather_main, weather_desc, temp_celsius, humidity
    else:
        return None

def print_weather_forecast(city, weather_main, weather_desc, temp_celsius, humidity):
    if weather_main is not None:
        print(f"Weather forecast for {city}:")
        print(f"Main weather: {weather_main}")
        print(f"Description: {weather_desc}")
        print(f"Temperature: {temp_celsius}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("Failed to fetch weather data.")

# Get city input from user
city = input("Enter a city name: ")

# Fetch and parse weather data
weather_data = fetch_weather(city)
weather_main, weather_desc, temp_celsius, humidity = parse_weather(weather_data)

# Print weather forecast
print_weather_forecast(city, weather_main, weather_desc, temp_celsius, humidity)

'