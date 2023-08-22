import requests
import datetime as dt
from decouple import config

APP_ID = config("APP_ID")
API_KEY = config("API_KEY")
AUTHORIZATION_KEY = config("AUTHORIZATION_KEY")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_KEY = config("SHEETY_KEY")
sheety_endpoint = f"https://api.sheety.co/{SHEETY_KEY}/myWorkouts/workouts"


exercise_text = input("Exercise: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

bearer_headers = {
  "Authorization": f"Bearer {AUTHORIZATION_KEY}"
}

exercise_params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 76,
    "height_cm": 178,
    "age": 20,
}

exercise_response = requests.post(exercise_endpoint, json=exercise_params, headers=headers)
exercise_response.raise_for_status()
result = exercise_response.json()

date = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%X")

for exercise in result["exercises"]:
  sheety_inputs = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise["user_input"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
    }
  }

  sheety_response = requests.post(
    sheety_endpoint,
    json=sheety_inputs,
    headers=bearer_headers)
  sheety_response.raise_for_status()
