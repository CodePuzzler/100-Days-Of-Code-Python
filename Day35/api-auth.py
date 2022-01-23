# Day35 of my 100DaysOfCode Challenge
# Example of API key authentication using open weather API
import requests

# authentication key
API_KEY = "YOUR-OWN-API-KEY"
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 28.585230,
    "lon": 76.374611,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWN_Endpoint, params=weather_params)
weather_data = response.json()

print(weather_data)

