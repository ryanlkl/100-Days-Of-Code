from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from manage_users import ManageUsers

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

dm = DataManager()
fs = FlightSearch()
nm = NotificationManager()
user = ManageUsers()

sheet_data = dm.get_data()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = fs.get_iata(row["city"])

    dm.destination_data = sheet_data
    dm.add_iata()

for row in sheet_data:
    data = fs.find_flight_prices(row["iataCode"])

    if data is None:
        continue
    
    price = data.price
    if row["lowestPrice"] > price:
      nm.send_message(
          price=price,
          from_airport=data.origin_airport,
          destination=data.destination_city,
          to_airport=data.destination_airport,
          from_date=data.out_date,
          to_date=data.return_date,
      )
      row["lowestPrice"] = price
      dm.destination_data = sheet_data
      dm.change_prices()
