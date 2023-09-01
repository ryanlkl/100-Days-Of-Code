import requests
from decouple import config
import datetime as dt
from flight_data import FlightData
from dateutil.relativedelta import relativedelta

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
HEADER = {
            "apikey": config("TEQUILA_API_KEY")
        }

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.city_codes = []
        tomorrow = dt.date.today() + dt.timedelta(days=1)
        self.tomorrow = tomorrow.strftime("%d/%m/%Y")
        six_months = tomorrow + relativedelta(months=+6)
        self.six_months = six_months.strftime("%d/%m/%Y")
        week = tomorrow + relativedelta(weeks=1)
        month = tomorrow + relativedelta(weeks=4)
        self.week = week.strftime("%d/%m/%Y")
        self.month = month.strftime("%d/%m/%Y")

    def get_iata(self,city_names: str):
        for city in city_names:
            endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
            params = {
                "term": city,
                "locale": "en-US"
            }
            response = requests.get(endpoint,params=params,headers=HEADER)
            data = response.json()
            code = data["locations"][0]["code"]
            self.city_codes.append(code)
        return self.city_codes

    def find_flight_prices(self,iata: str):
        endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        params = {
            "fly_from": "LON",
            "fly_to": iata,
            "date_from": self.tomorrow,
            "date_to": self.six_months,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "GBP",
            "max_stopovers": 0,
        }
        response = requests.get(endpoint,params=params,headers=HEADER)

        try:
            data = response.json()["data"][0]
        except IndexError:
            params["max_stopovers"] = 2
            response = requests.get(
                url=endpoint,
                params=params,
                headers=HEADER
            )
            data = response.json()["data"][0]
            print(f"No flights found for {iata}.")

            fd = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return fd
        else:
            fd = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=0,
                via_city=""
            )

            return fd
