import requests
from credentials import api_key

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : api_key,
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
print(response.status_code)
data = response.json()
daily_data = data["Time Series (Daily)"]
#Gather list of daily closing prices
closing_prices = [value["4. close"] for (key, value) in daily_data.items()]
print(closing_prices)
