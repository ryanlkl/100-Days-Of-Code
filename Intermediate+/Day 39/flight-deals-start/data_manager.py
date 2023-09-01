import requests
from decouple import config

SHEETY_API_KEY = config("SHEETY_API_KEY")
SHEETY_AUTHORIZATION = config("SHEETY_AUTHORIZATION")
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_API_KEY}/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.header = {
            "Authorization": f"Bearer {SHEETY_AUTHORIZATION}"
        }

    def get_data(self):
        response = requests.get(SHEETY_ENDPOINT,headers=self.header)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def add_iata(self):
        for city in self.destination_data:
            endpoint = f"{SHEETY_ENDPOINT}/{city['id']}"
            input = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(endpoint,json=input,headers=self.header)
            response.raise_for_status()

    def change_prices(self):
        for city in self.destination_data:
            endpoint = f"{SHEETY_ENDPOINT}/{city['id']}"
            input = {
                "price": {
                    "lowestPrice": city["lowestPrice"]
                }
            }
            response = requests.put(endpoint,json=input,headers=self.header)
            response.raise_for_status()
