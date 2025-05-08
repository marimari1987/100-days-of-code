import requests
from datetime import datetime, timedelta

MY_AIRPORT = "myariport"
TEQUILA_API = "insertapi"
tequila_endpoint = "https://tequila-api.kiwi.com/v2"
header = {
            "apikey": TEQUILA_API
        }


class FlightSearch:
    def search_flight(self, destination):
        today = datetime.now().date().strftime("%d/%m/%Y")
        six_months = (datetime.now() + timedelta(days=6 * 30)).strftime("%d/%m/%Y")
        stopovers = 1
        search_params = {
            "fly_from": MY_AIRPORT,
            "fly_to": destination,
            "dateFrom": today,
            "dateTo": six_months,
            "one_for_city": 1,
            "adults": 1,
            "max_stopovers": stopovers,
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 10,
            "flight_type": "round"

        }
        response = requests.get(url=f"{tequila_endpoint}/search", params=search_params, headers=header)
        response.raise_for_status()
        flights = response.json()["data"]

        if len(flights) == 0:
            stopovers += 1
            search_params["max_stopovers"] = stopovers
            response = requests.get(url=f"{tequila_endpoint}/search", params=search_params, headers=header)
            flights = response.json()["data"]
            if len(flights) == 0:
                return False

        for flight in flights:
            if flight["availability"]["seats"] is not None:
                return flight
            else:
                continue

    def get_iata_code(self, city):
        params = {
            "term": city
        }
        response = requests.get(url="https://tequila-api.kiwi.com/locations/query", headers=header,
                                params=params)
        data = response.json()
        iata_code = data["locations"][0]["code"]

        return iata_code
