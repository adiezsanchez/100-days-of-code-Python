import requests
import datetime as dt
MY_LAT = 63.435570
MY_LNG = 10.448210

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# The following splitting operations are done to obtain the hours in a 24h format
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
solar_noon = data["results"]["solar_noon"].split("T")[1].split(":")[0]
# Obtaining the current time
time_now = dt.datetime.now()
hour_now = time_now.hour
