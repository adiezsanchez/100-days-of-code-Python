import requests
from pprint import pprint
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "TEQUILA_API_KEY"


class FlightSearch:

    def get_destination_code(self, city_name):
        # Get TEQUILA API data and return IATA city code
        parameters = {
            "term":city_name
        }
        header = {"apikey":TEQUILA_API_KEY}
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/locations/query",
            headers = header,
            params=parameters
        )
        code = response.json()
        code = code["locations"][0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {"apikey":TEQUILA_API_KEY}

        query = {
            "fly_from": origin_city_code,
            "fly_to":destination_city_code,
            "dateFrom":from_time.strftime("%d/%m/%Y"),
            "dateTo":to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 14,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "NOK"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=header,
            params=query
        )
        flight_info = response.json()
        try:
            data = flight_info["data"][0]
            # pprint(data)
        except IndexError:
            print(f"No flights were found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        return flight_data
