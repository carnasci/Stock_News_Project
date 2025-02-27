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