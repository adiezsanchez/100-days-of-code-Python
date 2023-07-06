import requests
from twilio.rest import Client

# -------- OWM PARAMETER GLOBAL CONSTANTS ------- #
CITY= "Trondheim,NO"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "YOUR_API_KEY"
temp_API_KEY = "YOUR_TEMP_API_KEY"
LAT = 63.4305
LON = 10.395
EXCLUDE = "current,minutely,daily"

# -------- OWM API CALL AND RESPONSE ------- #
parameters = {
    "lat":LAT,
    "lon":LON,
    "exclude":EXCLUDE,
    "appid":temp_API_KEY
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

# -------- CHECK RAIN FORECAST FUNCTION ------- #
def bring_umbrella():

    for hour in weather_data["hourly"][:12]:
        weather = hour["weather"]
        weather_id = weather[0]["id"]
        if int(weather_id) < 700:
            return True

# -------- TWILIO API CONSTANTS ------- #
account_sid ='TWILIO_ACCOUNT_SID'
auth_token ='TWILIO_AUTH_TOKEN'
client = Client(account_sid, auth_token)

# -------- SENDING A WHATSAPP WITH TWILIO ------- #
def send_whatsapp():
    message = client.messages.create(
                                from_='whatsapp:+TWILIO_NUMBER',
                                body="It's going to rain today. Remember to bring an umbrella ☂️",
                                to='whatsapp:+YOUR_WHATSAPP_NUMBER'
                            )
    print(message.sid)
    print(message.status)

# -------- SENDING AN SMS WITH TWILIO ------- #
def send_sms():
    message = client.messages.create(
                                from_='+TWILIO_NUMBER',
                                body="It's going to rain today. Remember to bring an umbrella ☂️",
                                to='+YOUR_NUMBER'
                            )
    print(message.sid)
    print(message.status)
# -------- SEND NOTIFICATION IF RAIN ------- #
if bring_umbrella():
    send_sms()
