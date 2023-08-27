import requests
from twilio.rest import Client
from decouple import config

ACCOUNT_SID = config("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = config("TWILIO_AUTH_TOKEN")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.from_='+447723572174'
        self.to='+447307288855'

    def send_message(self,price,from_airport,destination,to_airport,from_date,to_date):
        client = Client(ACCOUNT_SID,AUTH_TOKEN)
        message = client.messages.create(
            from_=self.from_,
            body=f"Low Price alert! Only £{price} to fly from LONDON-{from_airport} to {destination}-{to_airport}, from {from_date} to {to_date}.",
            to=self.to,
        )
