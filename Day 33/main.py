import requests
from datetime import datetime
import smtplib
import time

MY_LONG =-0.127758
MY_LAT = 51.507351
MY_EMAIL = "pythonsmtp94@gmail.com"
MY_PASSWORD = "pkzqmcqayhihxbns"
SUBJECT = "Subject: ISS Overhead\n\n"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

iss_longitude = float(response.json()["iss_position"]["longitude"])
iss_latitude = float(response.json()["iss_position"]["latitude"])

iss_position = (iss_longitude,iss_latitude)

def overhead():
  if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
    return True

def is_night():
  parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
  }
  response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
  response.raise_for_status()
  data = response.json()
  sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
  sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
  time_now = datetime.now().hour

  if time_now >= sunset or time_now <= sunrise:
    return True

while True:
  time.sleep(300)
  if is_night and overhead:
    with smtplib.SMTP("smtp.gmail.com") as connection:
      connection.starttls()
      connection.login(user=MY_EMAIL,password=MY_PASSWORD)
      connection.sendmail(from_addr=MY_EMAIL,
                          to_addrs="ryanla94@gmail.com",
                          msg=f"{SUBJECT}The ISS is above you in the sky!")
