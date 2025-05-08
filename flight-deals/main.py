from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager
from pprint import pprint

flight_search = FlightSearch()
data_manager = DataManager()


# if sheet_data[0]["iataCode"] == "":
#     for row in sheet_data:
#         row["iataCode"] = flight_search.get_iata_code(row["city"])
#         iata_code = flight_search.get_iata_code(city)
#         data_manager.write_in_sheety(iata_code)

## Mein Code:
# for city in data_manager.read_cities():  # trägt den IATA Code in die Sheety Tabelle ein
#     iata_code = flight_search.get_iata_code(city)
#     data_manager.write_in_sheety(iata_code)

# destination_list = data_manager.read_iata()  # list mit PAR, IST....
destination_list = ["SFO"]

for destination in destination_list:
    flight = flight_search.search_flight(destination) 
    if not flight:
        print("no direct flight or a flight with one stopover available")
    else:
#        price_wish = data_manager.read_price(destination)
        price_wish = 800
        flight_data = FlightData(flight)
        pprint(flight)
        if flight_data.price < price_wish:
            text = f"{flight_data.price} Euro von {flight_data.departure_city} nach {flight_data.arrival_city}\n" \
                   f"{flight_data.outbound_date} bis {flight_data.inbound_date}" \
                   f" ({flight_data.nights_in_destination} Naechte)."
            if flight_data.has_stop_overs:
                text += f"Eine Zwischenlandung in {flight_data.stop_over}"
            text += f"Link: {flight_data.booking_link}"
            for user_email in data_manager.get_email_list():
                notification_manager = NotificationManager()
                notification_manager.send_email(text, user_email)
        else:
            print(f"No deal found. {flight_data.price} is the cheapest.")


## Links: https://tequila.kiwi.com/portal/docs/tequila_api/search_api
## https://dashboard.sheety.co/