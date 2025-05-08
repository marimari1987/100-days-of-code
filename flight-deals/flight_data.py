class FlightData:
    def __init__(self, flight):
        self.price = int(flight["conversion"]["EUR"])
        self.departure_city = flight["cityFrom"]
        self.departure_airport_iata_code = flight["flyFrom"]
        self.arrival_city = flight["cityTo"]
        self.arrival_airport_iata_code = flight["flyTo"]
        self.outbound_date = flight["route"][0]["local_departure"][:10]
        self.inbound_date = flight["route"][-1]["local_departure"][:10]
        self.nights_in_destination = flight["nightsInDest"]
        self.booking_link = flight["deep_link"]
        self.has_stop_overs = len(flight["route"]) > 2

        if self.has_stop_overs:
            for route in flight["route"]:
                city = route["cityFrom"]
                if city != self.arrival_city and city != self.departure_city:
                    self.stop_over = city
        else:
            self.inbound_date = flight["route"][1]["local_departure"][:10]

    # def is_deal(self, flight, price_wish):
    #     price = int(flight[0]["conversion"]["EUR"])
    #     if price < price_wish:
    #         return True
    #     else:
    #         return False
    #
    # def get_deal_details(self, flight):
    #     departure_city = flight[0]["cityFrom"]
    #     departure_airport_iata_code = flight[0]["flyFrom"]
    #     arrival_city = flight[0]["cityTo"]
    #     arrival_airport_iata_code = flight[0]["flyTo"]
    #     outbound_date = flight[0]["route"][0]["local_departure"][:10]
    #     price = int(flight[0]["conversion"]["EUR"])
    #     text = f"Flight from {departure_city} ({departure_airport_iata_code}) " \
    #            f"to {arrival_city} ({arrival_airport_iata_code}) on {outbound_date} costs only {price} €"
    #
    #     return text  # TODO: Anzahl stopovers angeben
