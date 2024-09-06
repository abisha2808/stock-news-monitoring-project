import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "H67HZY6IKIQBVWXF"
API_KEY2 = "c71bccf3ff1848418c35146a8992dd48"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameter ={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    # "interval": "60",
    "apikey": API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=parameter)
print(response.status_code)
#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
data = response.json()
print(data)
list = [value for (key, value) in data.items()]
yesterday_data = list[0]
yesterday_closed = yesterday_data["4. close"]
print(yesterday_closed)

#TODO 2. - Get the day before yesterday's closing stock price
day_before_data = list[1]
day_before_closed = day_before_data["4. close"]
print(day_before_closed)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_closed) - float(day_before_closed))
print(int(difference))
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = difference / float(yesterday_closed) * 100
print(percentage_difference)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_difference > 3:


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    parameter = {
        "q": STOCK_NAME,
        "apikey": API_KEY2
    }
    response = requests.get(NEWS_ENDPOINT, params=parameter)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



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

