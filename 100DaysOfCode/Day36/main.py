import requests
import os
from datetime import date, timedelta

STOCK = "TSLA"
API_URL = "https://www.alphavantage.co/query"
CLOSE_STRING = "4. close"
CALL_QUOTE = False
CALL_NEWS = True

quote_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ.get("ALPHA_STOCK_API_KEY")
}

news_parameters = {
    "function": "NEWS_SENTIMENT",
    "tickers": STOCK,
    "apikey": os.environ.get("ALPHA_STOCK_API_KEY")
}

def get_data(url, parameters):
    response = requests.get(url=url, params=parameters)
    response.raise_for_status()
    return response.json()

def get_quote():
    if CALL_QUOTE:
        qd = get_data(API_URL, quote_parameters)
        return qd["Time Series (Daily)"]
    else:
        return {'2024-06-04': {'1. open': '1157.1500', '2. high': '1166.0000', '3. low': '1140.4500', '4. close': '1164.3700', '5. volume': '40222547'}, '2024-06-03': {'1. open': '1136.2100', '2. high': '1150.0000', '3. low': '1120.0300', '4. close': '1150.0000', '5. volume': '43839176'}, '2024-05-31': {'1. open': '1125.2000', '2. high': '1127.1700', '3. low': '1069.4000', '4. close': '1096.3300', '5. volume': '61326250'}, '2024-05-30': {'1. open': '1146.5000', '2. high': '1158.1915', '3. low': '1096.6300', '4. close': '1105.0000', '5. volume': '48735033'}, '2024-05-29': {'1. open': '1130.5000', '2. high': '1154.9200', '3. low': '1109.0100', '4. close': '1148.2500', '5. volume': '55744193'}}

def get_news():
    if CALL_NEWS:
        nd = get_data(API_URL, news_parameters)
        return nd["feed"]
    else:
        feed_data = [{'title': 'Elon Musk sets record straight on Nvidia AI chip shipments', 'url': 'https://cointelegraph.com/news/elon-musk-sets-responds-nvidia-ai-chip-shipments', 'time_published': '20240604T203303', 'authors': ['Vince Quill'], 'summary': "The billionaire industrialist clarified that the south extension of Tesla's Giga Factory in Texas would soon be complete, allowing for more AI infrastructure.", 'banner_image': 'https://images.cointelegraph.com/cdn-cgi/image/format=auto,onerror=redirect,quality=90,width=1200/https://s3.cointelegraph.com/uploads/2024-06/ed62c2ee-5b63-4d82-b259-35956569091a.jpg', 'source': 'Cointelegraph', 'category_within_source': 'n/a', 'source_domain': 'cointelegraph.com', 'topics': [{'topic': 'Technology', 'relevance_score': '0.5'}, {'topic': 'Manufacturing', 'relevance_score': '0.5'}], 'overall_sentiment_score': -0.018972, 'overall_sentiment_label': 'Neutral', 'ticker_sentiment': [{'ticker': 'GOOG', 'relevance_score': '0.09989', 'ticker_sentiment_score': '0.103051', 'ticker_sentiment_label': 'Neutral'}, {'ticker': 'NVDA', 'relevance_score': '0.384397', 'ticker_sentiment_score': '-0.03466', 'ticker_sentiment_label': 'Neutral'}, {'ticker': 'TSLA', 'relevance_score': '0.620415', 'ticker_sentiment_score': '-0.135249', 'ticker_sentiment_label': 'Neutral'}]}, {'title': "What's Going On With Super Micro Computer Stock On Tuesday? - Super Micro Computer  ( NASDAQ:SMCI ) ", 'url': 'https://www.benzinga.com/news/24/06/39169883/whats-going-on-with-super-micro-computer-stock-on-tuesday', 'time_published': '20240604T195056', 'authors': ['Anusuya Lahiri'], 'summary': 'AI server vendor Super Micro Computer, Inc SMCI stock traded lower Tuesday in sympathy with the broader semiconductor industry as Taiwan Semiconductor Manufacturing Co TSM weighs price hikes for its AI chip production services as per a Nikkei Asia report.', 'banner_image': 'https://cdn.benzinga.com/files/images/story/2024/06/04/Super-Micro-Computer.jpeg?width=1200&height=800&fit=crop', 'source': 'Benzinga', 'category_within_source': 'News', 'source_domain': 'www.benzinga.com', 'topics': [{'topic': 'Technology', 'relevance_score': '0.5'}, {'topic': 'Financial Markets', 'relevance_score': '0.905476'}, {'topic': 'Manufacturing', 'relevance_score': '0.5'}], 'overall_sentiment_score': 0.496836, 'overall_sentiment_label': 'Bullish', 'ticker_sentiment': [{'ticker': 'NVDA', 'relevance_score': '0.247838', 'ticker_sentiment_score': '0.275784', 'ticker_sentiment_label': 'Somewhat-Bullish'}, {'ticker': 'AAPL', 'relevance_score': '0.247838', 'ticker_sentiment_score': '0.275784', 'ticker_sentiment_label': 'Somewhat-Bullish'}, {'ticker': 'INTC', 'relevance_score': '0.472338', 'ticker_sentiment_score': '0.498205', 'ticker_sentiment_label': 'Bullish'}, {'ticker': 'SMCI', 'relevance_score': '0.247838', 'ticker_sentiment_score': '0.015201', 'ticker_sentiment_label': 'Neutral'}, {'ticker': 'TSM', 'relevance_score': '0.247838', 'ticker_sentiment_score': '0.015201', 'ticker_sentiment_label': 'Neutral'}]}, {'title': 'Microsoft Forges Billion-Dollar AI Deal With Hitachi - Hitachi  ( OTC:HTHIF ) , Amazon.com  ( NASDAQ:AMZN ) ', 'url': 'https://www.benzinga.com/news/earnings/24/06/39164667/microsoft-forges-billion-dollar-ai-deal-with-hitachi', 'time_published': '20240604T193644', 'authors': ['Zacks'], 'summary': 'Microsoft MSFT has announced a major strategic alliance with Japanese industrial conglomerate Hitachi Ltd. HTHIF, which is projected to involve multibillion-dollar investments over the next three years.', 'banner_image': 'https://cdn.benzinga.com/files/images/story/2024/06/04/matthew-manuel-bhlsbx-0rnm-unsplash.jpg?width=1200&height=800&fit=crop', 'source': 'Benzinga', 'category_within_source': 'Trading', 'source_domain': 'www.benzinga.com', 'topics': [{'topic': 'Retail & Wholesale', 'relevance_score': '0.333333'}, {'topic': 'Financial Markets', 'relevance_score': '0.161647'}, {'topic': 'Manufacturing', 'relevance_score': '0.333333'}, {'topic': 'Earnings', 'relevance_score': '0.158519'}, {'topic': 'Technology', 'relevance_score': '0.333333'}], 'overall_sentiment_score': 0.361046, 'overall_sentiment_label': 'Bullish', 'ticker_sentiment': [{'ticker': 'MSFT', 'relevance_score': '0.419385', 'ticker_sentiment_score': '0.412383', 'ticker_sentiment_label': 'Bullish'}, {'ticker': 'META', 'relevance_score': '0.087985', 'ticker_sentiment_score': '0.154677', 'ticker_sentiment_label': 'Somewhat-Bullish'}, {'ticker': 'NVDA', 'relevance_score': '0.131643', 'ticker_sentiment_score': '0.145521', 'ticker_sentiment_label': 'Neutral'}, {'ticker': 'HTHIF', 'relevance_score': '0.259727', 'ticker_sentiment_score': '0.357216', 'ticker_sentiment_label': 'Bullish'}, {'ticker': 'AMZN', 'relevance_score': '0.131643', 'ticker_sentiment_score': '-0.02731', 'ticker_sentiment_label': 'Neutral'}]}]
        return feed_data

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_series = [value for (key, value) in get_quote().items()]

ys_close_price = float(stock_series[0][CLOSE_STRING])
dbfys_close_price = float(stock_series[1][CLOSE_STRING])
print(f"Yesterday Price: {ys_close_price}\nDay before yesterday Price: {dbfys_close_price}")

five_percent = ys_close_price * 0.05

if (abs(ys_close_price - dbfys_close_price) > five_percent):
    print("Get News!")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_data = get_news()
top_3_news = news_data[:3]
for item in top_3_news:
    print(f"News: {item['title']}, URL: {item['url']}")
       

    

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