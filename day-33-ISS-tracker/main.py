import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 63.435570 # Your latitude
MY_LONG = 10.448210 # Your longitude

my_email = "adiez.biotech@gmail.com"
to_email = "alberto.d.sanchez@ntnu.no"
app_password = "sghs klth krtj dued"

def is_above():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (iss_latitude - 5) <= MY_LAT <= (iss_latitude + 5) and (iss_longitude - 5) <= MY_LONG <= (iss_longitude + 5):
        return True
    else:
        return False

    #Your position is within +5 or -5 degrees of the ISS position.

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    hour_now = time_now.hour

    if sunrise <= hour_now <= sunset:
        return False
    else:
        return True

while True:
    # Run the code every 60 seconds
    time.sleep(60)
    print(is_above())
    print(is_night())
    if is_above() and is_night():
        print("Go out")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # Securing our connection to the e-mail server (encryption)
            connection.starttls()
            # Login:
            connection.login(user=my_email, password=app_password)
            # Sending mail
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg="Subject:ISS Tracker\n\nLook up!."
            )
            # Once it reaches this point the connection is closed since we are using the "with" method.

    else:
        print("Keep waiting")



