import requests

# https://openweathermap.org/api

API_KEY = "0d289103231d1d75151df1cead89bf02"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Please provide a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Weather: ", weather)
    print("Temperature: ", temperature)

else:
    print("An error occured")