import requests
from twilio.rest import Client

# -------- NEWS API PARAMETER GLOBAL CONSTANTS ------- #
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"

# -------- STOCK API PARAMETER GLOBAL CONSTANTS ------- #
STOCK_NAME = "BABA"
COMPANY_NAME = "Alibaba"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "YOUR_STOCK_API_KEY"

# -------- TWILIO API CONSTANTS ------- #
account_sid = 'TWILIO_ACCOUNT_SID'
auth_token = 'TWILIO_AUTH_TOKEN'
client = Client(account_sid, auth_token)

# -------- SENDING A WHATSAPP WITH TWILIO ------- #
def send_whatsapp(headline, brief, difference, current, previous):
    if current > previous:
        symbol = "🔺"
    else:
        symbol = "🔻"
    message = client.messages.create(
        from_='whatsapp:+TWILIO_NUMBER',
        body=f"{STOCK_NAME}: {symbol}{difference}% \nHeadline: {headline} \nBrief: {brief}",
        to='whatsapp:+YOUR_NUMBER'
    )
    print(message.sid)
    print(message.status)

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
# -------- STOCK API CALL AND RESPONSE ------- #

stock_parameters = {
    "function":"TIME_SERIES_INTRADAY",
    "symbol":STOCK_NAME,
    "interval":"60min",
    "adjusted":"true",
    "apikey":STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT,params=stock_parameters)
response.raise_for_status()
stock_data = response.json()

daily_prices = [value for (key, value) in stock_data["Time Series (60min)"].items()]
closing_prices = [item["4. close"] for item in daily_prices]
current = float(closing_prices [0])

#TODO 2. - Get the day before yesterday's closing stock price
previous = float(closing_prices [16])
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
difference = round(abs(current - previous) / previous * 100, 1)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if difference >= 5:

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

    news_parameters = {
        "qInTitle":COMPANY_NAME,
        "sortBy":"popularity",
        "apiKey":NEWS_API_KEY
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()
    list_of_articles = articles["articles"]

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    top_3_news = list_of_articles[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    news_headline_description = [[item["title"], item["description"]] for item in top_3_news]
    print(news_headline_description)

#TODO 9. - Send each article as a separate message via Twilio. 

    for news in news_headline_description:
        headline = news[0]
        brief = news[1]
        send_whatsapp(headline, brief, difference, current, previous)
        print("Message sent")

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

