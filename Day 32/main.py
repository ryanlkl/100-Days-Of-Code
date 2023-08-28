import smtplib
import datetime as dt
import random
from email.message import EmailMessage
from decouple import config

# my_email = "pythonsmtp94@gmail.com"
# password = "pkzqmcqayhihxbns"


# with smtplib.SMTP("smtp.gmail.com") as connection:
#   connection.starttls()
#   connection.login(user=my_email,password=password)
#   connection.sendmail(from_addr=my_email,
#                       to_addrs="ryanla94@gmail.com",
#                       msg="Subject: Hello Ryan!\n\nThis is the email body")

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# weekday = now.weekday()

# date_of_birth = dt.datetime(year=2003,month=3,day=15)

PRIVATE_EMAIL = config("PRIVATE_EMAIL")
MY_EMAIL = config("MY_EMAIL")
MY_PASSWORD = config("MY_PASSWORD")
SUBJECT = "Monday Motivation"

day_today = dt.datetime.now().weekday()
if day_today == 4:
  with open("Day 32\\quotes.txt", encoding="utf-8") as quotes:
      all_quotes = quotes.readlines()
      msg = random.choice(all_quotes)

  with smtplib.SMTP("smtp.gmail.com") as connection:
     connection.starttls()
     connection.login(MY_EMAIL,MY_PASSWORD)
     connection.sendmail(from_addr=MY_EMAIL,
                         to_addrs="ryanla94@gmail.com",
                         msg=f"Subject:{SUBJECT}\n\n{msg}".encode("utf-8"))
