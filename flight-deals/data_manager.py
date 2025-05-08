import requests
import pandas
import os


class DataManager:
    def __init__(self):
        self.id = 2
        self.TOKEN = os.environ.get("SHEETY_TOKEN")
        self.header = {
            "ContentType": "application/json",
            "Authorization": f"Bearer {self.TOKEN}"
        }

    def write_in_sheety(self, iata_code):
        params = {
            "price": {
                "iataCode": iata_code,
            }
        }
        response = requests.put(
            url=f"https://api.sheety.co/5acffa06d552e4a34c442345f24f9983/flightDeals/prices/{self.id}",
            headers=self.header,
            json=params)

        self.id += 1
        # wenn man nicht weiß wie genau die Parameter Namen sind, am besten einmal requests.get() und dann resposne.text
        print(response.text)

    def read_cities(self):
        response = requests.get("https://api.sheety.co/5acffa06d552e4a34c442345f24f9983/flightDeals/prices",
                                headers=self.header)
        cities = response.json()["prices"]
        city_list = [city["city"] for city in cities]
        return city_list

    def read_iata(self):
        response = requests.get("https://api.sheety.co/5acffa06d552e4a34c442345f24f9983/flightDeals/prices",
                                headers=self.header)
        data = response.json()["prices"]
        iata_list = [iata_code["iataCode"] for iata_code in data]
        return iata_list

    def read_price(self, destination):
        response = requests.get("https://api.sheety.co/5acffa06d552e4a34c442345f24f9983/flightDeals/prices",
                                headers=self.header)
        data = response.json()["prices"]
        data_frame = pandas.DataFrame(data)
        price = int(data_frame[data_frame.iataCode == destination]["lowestPrice"])
        return price

    def get_email_list(self):
        response = requests.get("https://api.sheety.co/5acffa06d552e4a34c442345f24f9983/flightDeals/user",
                                headers=self.header)
        users = response.json()["user"]
        email_list = [user["email"] for user in users]
        return email_list

