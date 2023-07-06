import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# This snippet of code below provides info on the error if there is one
response.raise_for_status()

data = response.json()
print(data)
iss_position = (data["iss_position"]["latitude"], data["iss_position"]["longitude"])
print(iss_position)