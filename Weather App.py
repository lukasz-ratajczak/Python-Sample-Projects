# Weather App

# Setup
import json, requests

# Setting location - example Gdansk - 54.372158, 18.638306


lat = input("Enter your latitude: ")
lon = input("Enter your longitude: ")

# Api openweather.org - hidden key
with open('misc.json') as f:
    api_key = json.load(f)['api_keys']['openweather']

# Getting data from website
r = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}")

print(r)