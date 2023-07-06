from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

input_city = input("Where do you want to fly from?: ")
ORIGIN_CITY_IATA = flight_search.get_destination_code(input_city)
print(ORIGIN_CITY_IATA)

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    try:
        if flight.price < destination["lowestPrice"]:

            users = data_manager.get_customer_emails()
            #List comprehension to iterate over elements of a list
            emails = [row["email"] for row in users]

            message = f"Low price alert! Only NOK{flight.price} " \
                      f"to fly from {flight.origin_city}-{flight.origin_airport} " \
                      f"to {flight.destination_city}-{flight.destination_airport}, " \
                      f"from {flight.out_date} to {flight.return_date}." \

            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            # This line adds the Google flight link to buy the flight:
            google_flight_link= f'\nhttps://www.google.com/travel/flights?q=Flights%20to%20' \
                       f'{flight.destination_airport}%20from%20{flight.origin_airport}%20on%20' \
                       f'{flight.out_date}%20through%20{flight.return_date}'

            print(message, google_flight_link)
            # This method below sends a Whatsapp notification (commented out)
            # notification_manager.send_whatsapp(message=message)
            # This method below sends an e-mail notification
            notification_manager.send_email(message=message, google_flight_link=google_flight_link, emails=emails)
        if flight.price > destination["lowestPrice"]:
            print(f"Flights were more expensive than your target range for {destination['city']}")
        else:
            pass
    except AttributeError:
        pass

# Reset the Flight_Deals spreadsheet (erase IATA codes)
for row in sheet_data:
    row["iataCode"] = ""
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()