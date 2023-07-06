import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/5aaba5e5840d27a7f6e38035bc08fbe0/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/5aaba5e5840d27a7f6e38035bc08fbe0/flightDeals/users"
SHEETY_USERNAME = "SHEETY_USERNAME"
SHEETY_PASS = "SHEETY_PASS"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=(SHEETY_USERNAME, SHEETY_PASS))
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                auth = (SHEETY_USERNAME, SHEETY_PASS),
                json=new_data
            )

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, auth=(SHEETY_USERNAME, SHEETY_PASS))
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
