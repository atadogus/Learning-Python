import requests
import datetime as dt
import os

# os is a module used for hiding confidential information such as a password using environment variables
# the information is stored in the local system and (my computer) and a key is used to access it
# https://www.youtube.com/watch?v=IolxqkL7cD8 -> "ortam değişkenleri"

STOCK = "TESLA"
COMPANY_NAME = "Tesla Inc"

# TODO 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK_API_KEY = os.environ.get("stock_key")

stock_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "IBM",
    "interval": "60min",
    "apikey": STOCK_API_KEY
}

stock_request = requests.get("https://www.alphavantage.co/query", params=stock_parameters).json()
for key in stock_request:
    for inner_key in stock_request[key]:
        print(f"{inner_key}: {stock_request[key][inner_key]}")

# TODO 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

NEWS_API_KEY = os.environ.get("news_key")
today = dt.datetime.now()

news_parameters = {
    "q": "Tesla",
    "from": f"{today.year}-{today.month}-{today.day}",
    "apiKey": NEWS_API_KEY
}


news_request = requests.get("https://newsapi.org/v2/everything", params=news_parameters).json()

for article in news_request["articles"]:
    print(article)


# TODO 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


# TODO Optional: Format the SMS message like this:

"""
TESLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TESLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TESLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TESLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
