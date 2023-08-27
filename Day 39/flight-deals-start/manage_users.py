import requests
from decouple import config

API_KEY = config("SHEETY_API_KEY")
AUTHORIZATION = config("SHEETY_AUTHORIZATION")

class ManageUsers:

    def __init__(self):
        self.header = {
            "Authorization": f"Bearer {AUTHORIZATION}"
        }
        print("Welcome to Ryan's Flight Club.")
        print("We find the best flight deals and email you.")
        self.endpoint = f"https://api.sheety.co/{API_KEY}/flightDeals/users"
        self.first_name = input("What is you first name?\n")
        self.last_name = input("What is your last name?\n")
        self.email = input("What is your email?\n")
        self.add_user(self.first_name,self.last_name,self.email)

    def add_user(self,first,last,email):
        input = {
            "user": {
                "firstName": first,
                "lastName": last,
                "email": email,
            }
        }
        response = requests.post(self.endpoint,params=input,headers=self.header)
        response.raise_for_status()
