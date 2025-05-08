import requests
import os
from datetime import datetime

APP_ID = os.environ.get("APP_ID_NUTRITIONIX")
API_KEY = os.environ.get("API_KEY_NUTRITIONIX")
TOKEN = os.environ.get("SHEETY_TOKEN")
MY_GENDER = "female"
MY_WEIGHT = 74
MY_HEIGHT = 183
MY_AGE = 33

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

parameters = {
    "query": input("Tell me what exercise you did  ".lower()),
    "gender": MY_GENDER,
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": MY_AGE
}

response = requests.post(url=" https://trackapi.nutritionix.com/v2/natural/exercise", headers=header, json=parameters)
data = response.json()
print(response)

for exercises in data["exercises"]:
    exercise = exercises["name"]
    duration = exercises["duration_min"]
    calories = exercises["nf_calories"]

    google_sheety_endpoint = os.environ.get("SHEETY_ENDOINT")
    today = datetime.now().strftime("%d/%m/%Y")
    time = str(datetime.now().time())[:8]

    bearer_header = {
        "ContentType": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

    workout_parameters = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories
        }
    }

    response = requests.post(url=google_sheety_endpoint, json=workout_parameters, headers=bearer_header)
    print(response)
