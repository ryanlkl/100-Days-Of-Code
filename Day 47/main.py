import requests
from bs4 import BeautifulSoup
import smtplib
from decouple import config

provider = "smtp.gmail.com"

PRIVATE_EMAIL = config("PRIVATE_EMAIL")
MY_EMAIL = config("MY_EMAIL")
MY_PASSWORD = config("MY_PASSWORD")
BUY_PRICE = 200
URL = "https://www.amazon.co.uk/Portable-Mechanical-Keyboard-Minimalist-Convenient/dp/B09YV448ZY/ref=sr_1_4?crid=L3Y149K4I8V4&keywords=white%2Bmechanical%2Bkeyboard&qid=1693235122&sprefix=white%2Bmechanical%2Bkeyboar%2Caps%2C87&sr=8-4&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB",
}

response = requests.get(URL,headers=header)
data = response.content

soup = BeautifulSoup(data,"html.parser")
price = soup.find(name="span",class_="a-offscreen").getText()
price_without_currency = price.split("£")[1]
price_as_float = float(price_without_currency)
title = soup.find(id="productTitle").getText().strip()

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(provider) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=PRIVATE_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
