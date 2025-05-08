import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
yesterday = datetime.now().date() - timedelta(days=1)  # Beispiel date yesterday
day_before_yesterday = yesterday - timedelta(days=1)

load_dotenv("path/.env.txt")
api_key_av = os.environ.get("AV_STOCK_KEY")
api_key_news = os.environ.get("NEWS_API_KEY")

parameters_av = {"function": "TIME_SERIES_DAILY",
                 "symbol": STOCK,
                 "apikey": api_key_av
                 }

parameters_news = {"q": COMPANY_NAME,
                   "from": str(yesterday),
                   "sortBy": "popularity",
                   "apikey": api_key_news
                   }

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

response_av = requests.get(url="https://www.alphavantage.co/query", params=parameters_av)
response_av.raise_for_status()

stock_value_yesterday = float(response_av.json()["Time Series (Daily)"][str(yesterday)]["4. close"])
stock_value_before_yesterday = float(response_av.json()["Time Series (Daily)"][str(day_before_yesterday)]["4. close"])
text = ""

stock_difference = abs(stock_value_yesterday - stock_value_before_yesterday)
percent = round((stock_difference / stock_value_yesterday) * 100, 2)

if stock_value_yesterday > stock_value_before_yesterday:
    text += f"TSLA: 🔺 {percent} %\n"
else:
    text += f"TSLA: 🔻 {percent} %\n"

if percent > 0:
    response_news = requests.get(url="https://newsapi.org/v2/everything", params=parameters_news)
    response_news.raise_for_status()
    articles = response_news.json()["articles"][:3]
    for article in articles:
        text += f"Title: {article['title']}\nBrief: {article['description']}\n"
#     account_sid = os.environ.get("TWILIO_SID")
#     auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#                          body=text,
#                          from_='+18179845545',
#                          to='+491781479925'
#                     )

print(stock_value_yesterday)
print(stock_value_before_yesterday)
print(text)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

