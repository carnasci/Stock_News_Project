import requests
from twilio.rest import Client
from credentials import api_key, news_api_key, acc_sid, auth_token

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
positive_difference = (yesyesterday_closing - yesterday_closing)
up_down = ""
if positive_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
print(positive_difference)
percent_diff = (abs(positive_difference)/yesyesterday_closing)*100
print(percent_diff)
if percent_diff > 3:
    #print("Get News")
    #Instead of printing get news get the first 3 news articles for the company
    news_parameters = {
        "q" : COMPANY_NAME,
        "language" : "en",
        "searchIn" : "title,description",
        "apikey" : news_api_key,
    }
    response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_data = response.json()
    first_three_articles = news_data["articles"][:3]
    print(first_three_articles)
    formatted_articles = [f"{STOCK_NAME}: {up_down}{round(percent_diff, 2)}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in first_three_articles]
    print(formatted_articles)

    client = Client(acc_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body=f"{article}",
            to="whatsapp:+13147286668"
        )
        print(message.status)
