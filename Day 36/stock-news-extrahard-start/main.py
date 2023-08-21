import requests
from twilio.rest import Client
from decouple import config

# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_KEY = config("STOCK_KEY")
NEWS_KEY = config("NEWS_KEY")
ACCOUNT_SID = config("ACCOUNT_SID")
AUTH_TOKEN = config("AUTH_TOKEN")

AV_ENDPOINT = "https://www.alphavantage.co/query"
AV_FUNCTION = "TIME_SERIES_DAILY"
av_params = {
    "function": AV_FUNCTION,
    "symbol": STOCK,
    "apikey": STOCK_KEY
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_KEY
}

# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Get stock data
stock_response = requests.get(AV_ENDPOINT, params=av_params)
stock_response.raise_for_status()
stock_data = stock_response.json()
dates = stock_data["Time Series (Daily)"]
days = list(dates.keys())[0:2]
day_1 = dates[days[0]]["4. close"]
day_2 = dates[days[1]]["4. close"]
perc_diff = round(((float(day_1) - float(day_2)) / float(day_2)) * 100, 3)
sign = "🔺" if perc_diff > 0 else "🔻"

# Check stock price change and fetch news
if abs(perc_diff) > 1:
    news_response = requests.get(
        f'https://newsapi.org/v2/everything?qInTitle="{COMPANY_NAME}"&apiKey={NEWS_KEY}'
    )
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    first_3 = articles[:3]

    # Send SMS messages
    for a in first_3:
        message = client.messages.create(
            from_="+447723572174",
            body=f"TSLA: {sign}{abs(perc_diff)}%\nHeadline: {a['title']}",
            to="+447307288855"
        )
