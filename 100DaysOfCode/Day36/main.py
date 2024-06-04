import requests
import os
from datetime import date, timedelta

STOCK = "NVDA"
COMPANY_NAME = "NVIDIA Inc"
API_URL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"
CLOSE_STRING = "4. close"

parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": os.environ.get("ALPHA_STOCK_API_KEY")
    }

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url=API_URL, params=parameters)
response.raise_for_status()
data = response.json()
stock_series = data["Time Series (Daily)"]

yesterday = date.today() - timedelta(days=3)
day_before_yesterday = yesterday - timedelta(days=1)
ys_string = f'{yesterday:%Y-%m-%d}'
dbfys_string = f'{day_before_yesterday:%Y-%m-%d}'

ys_close_price = float(stock_series[ys_string][CLOSE_STRING])
dbfys_close_price = float(stock_series[dbfys_string][CLOSE_STRING])
print(f"Yesterday: {ys_string}\t Close Price: {ys_close_price}\nDay before yesterday: {dbfys_string}\t Close Price: {dbfys_close_price}")

five_percent = ys_close_price * 0.05

if (abs(ys_close_price - dbfys_close_price) > five_percent):
    print("Get News!")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

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