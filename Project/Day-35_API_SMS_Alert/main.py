import requests
from twilio.rest import Client
import os


# API_KEY = "53c33d7ed404e36113b3ec87cf1f5f54"
API_KEY = "f4bc1306c8c0bda6307d0dc8941437a4"
# account_sid = os.environ["AC1176d4eae6a0032a307cf6e8176614dd"]
# auth_token = os.environ["0e88bc1337456d3cf3f99dd6f902001e"]

account_sid ="AC1176d4eae6a0032a307cf6e8176614dd"
auth_token ="0e88bc1337456d3cf3f99dd6f902001e"




url = "https://api.openweathermap.org/data/3.0/onecall"

weather_params = {
    "lat":1.460126,
    "lon":124.826347,
    "appid":API_KEY,
    "exclude":"current,minutely,daily"
}

response = requests.get(url,params=weather_params)
response.raise_for_status()
# data = response.json()["hourly"][0]["weather"][0]
weather_data = response.json()
weather_slicing = weather_data["hourly"][:12]
will_rain = False

for hour_data in weather_slicing:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700 :
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_="+15703739786",
        to="+62856494040")
    print(message.status)

# for id in range (0,7):
#     if data[id]["weather"][0]["id"] < 700:
#         print ("Bring umbrella")

# test = data[0]["weather"][0]["id"]
