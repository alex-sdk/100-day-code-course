import requests
import os

auth_token = os.environ.get('weather_token')

weather_params = {
    'lat':43.651070,
    'lon':-79.347015,
    'appid': auth_token,
    'exclude': 'current,minutely,daily',
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=weather_params)
response.raise_for_status()
data = response.json()
print(data)

will_rain = False
#checks if it will rain at specified long lat within 12 hour period
for hour in range(12):
    if data['hourly'][hour]['weather'][0]['id'] < 700:
        will_rain = True
        break
if will_rain:
    print("It will rain")