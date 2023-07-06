import requests
import os
from datetime import datetime


# -------------- NUTRITIONIX API -----------------------

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 180
AGE = 32

APP_ID = "YOUR_APP_ID"
API_KEY = "YOUR_API_KEY"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2"

exercise_input = input("Tell me which exercises you did: ")

parameters = {
    "query":exercise_input,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}

header = {
    "x-app-id": APP_ID,
    "x-app-key":API_KEY,
    "x-remote-user-id":"0"
}

response = requests.post(url=f"{nutritionix_endpoint}/natural/exercise",  json=parameters, headers=header)
result = response.json()
print(result)

# -------------- SHEETY API -----------------------

SHEETY_USERNAME = "SHEETY_USERNAME"
SHEETY_PASS = "SHEETY_PASS"

sheety_endpoint = "https://api.sheety.co/5aaba5e5840d27a7f6e38035bc08fbe0/workoutTracking/workouts"
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(url=sheety_endpoint,  json=sheet_inputs, auth=(SHEETY_USERNAME, SHEETY_PASS))
    sheety_result = sheety_response.json()
    print(sheety_result)
