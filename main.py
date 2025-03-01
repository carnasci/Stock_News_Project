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
print(data)
daily_data = data["Time Series (Daily)"]
#Gather list of daily closing prices
closing_prices = [value["4. close"] for (key, value) in daily_data.items()]
print(closing_prices)
yesterday_closing = float(closing_prices[0])
yesyesterday_closing = float(closing_prices[1])
positive_difference = abs(yesyesterday_closing - yesterday_closing)
print(positive_difference)
percent_diff = (positive_difference/yesyesterday_closing)*100
print(percent_diff)
if percent_diff > 5:
    print("Get News")

