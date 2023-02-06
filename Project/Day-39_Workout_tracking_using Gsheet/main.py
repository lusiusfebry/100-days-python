import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
# BEARER_AUTH = "Dlsu2000"
AUTH_BEARER = {
    "Authorization": "Bearer Dlsu2000"
}

# query = input ("What is your exercise: ")
# gender = input("What is your gender: ")

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

query = input("Tell me which exercise you did ? ")
exercise_config = {
    "query": query,
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=exercise_headers)
result = response.json()

# sheet_endpoint = "https://api.sheety.co/d22cf19f2fe054e081ab33ee42ef4b03/myWorkouts/workouts"
sheet_endpoint = os.environ.get("sheet_endpoint")
now = datetime.now()
today_date = now.strftime("%d/%m/%Y")
today_time = now.strftime("%X")

for data in result["exercises"]:
    input_sheet = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": data["name"].title(),
            "duration": data["duration_min"],
            "calories": data["nf_calories"]

        }
    }

    input_to_sheet = requests.post(url=sheet_endpoint, json=input_sheet,headers=AUTH_BEARER)
    print(input_to_sheet.text)
