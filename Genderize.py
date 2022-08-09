# Gender Guess REST App

# Setup

import requests

# App

name = input("Enter your name: ")

r = requests.get(f"https://api.genderize.io/?name={name}")

print(f"You are {r.json()['gender'].upper()} with probability of {float(r.json()['probability'])*100}%")