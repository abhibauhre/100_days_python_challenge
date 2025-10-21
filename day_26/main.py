import requests
from twilio.rest import Client
import os

OWN_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OPENWEATHER_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")


weather_params = {
    "lat": 28.535517,
    "lon": 77.391029,  
    "appid": api_key,
    "cnt":4,
}

response = requests.get(OWN_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for data in weather_data["list"]:
    condition_code = data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_='+12295958296',
        to=os.environ.get("TO_PHONE_NUMBER")
    )

    print(message.status)
