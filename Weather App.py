# Weather App

# Setup
import json, requests, datetime

lang = 'en' # pl - for polish. More information -> openweathermap.org

# Setting location - example Gdansk - 54.372158, 18.638306


lat = input("Enter your latitude: ")
lon = input("Enter your longitude: ")
print("--------------")
#lat = 54.372158
#lon = 18.638306

# Api openweather.org - hidden key
with open('misc.json') as f:
    api_key = json.load(f)['api_keys']['openweather']

# Getting data from website
r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&lang={lang}&appid={api_key}")

desc = r.json()['weather'][0]['description']
temp = r.json()['main']['temp']
temp_min = r.json()['main']['temp_min']
temp_max = r.json()['main']['temp_max']
pressure = r.json()['main']['pressure']
humidity = r.json()['main']['humidity']
wind = r.json()['wind']['speed']
sunrise = r.json()['sys']['sunrise']
sunset =  r.json()['sys']['sunset']
name = r.json()['name']

print(f'In {name}, Weather: {desc}, Temperature: {temp}C, Pressure: {pressure}hPa, Humidity: {humidity}%, Wind speed: {wind}kmh, Sunrise: {datetime.datetime.fromtimestamp(sunrise).strftime("%H:%M:%S")}, Sunset: {datetime.datetime.fromtimestamp(sunset).strftime("%H:%M:%S")}')