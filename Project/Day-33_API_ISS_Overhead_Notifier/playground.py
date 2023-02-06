import requests
from datetime import datetime
# url="http://api.open-notify.org/iss-now.json"
# response = requests.get(url)
#
# # data = test.json()["iss_position"].get("latitude")
# latitude =response.json()["iss_position"]["latitude"]
# longitude =response.json()["iss_position"]["longitude"]
#
# iss_position = (longitude,latitude)
# print(iss_position)
MY_LAT = -0.789275
MY_LNG = 113.921326
parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LNG,
    "formatted" : 0,
}
url = "https://api.sunrise-sunset.org/json"
response = requests.get(url,params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)

time_now = datetime.now()
print(time_now.hour)
