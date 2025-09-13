import requests
from twilio.rest import Client

account_sid = 'enter your twillio account sid'
auth_token = 'enter your twillio auth token'

stock_api_key="enter your stock api key"
news_api_key='enter your news api key'

stock_name='TSLA'             # it specifies only tesla shares
company_name='Tesla Inc'      # it specifies company 

stocks_endpoint='https://www.alphavantage.co/query'
news_endpoint='https://newsapi.org/v2/everything'

stocks_param={
    'function':'TIME_SERIES_DAILY',
    'symbol':stock_name,
    'apikey':stock_api_key,
}
news_param={
    'apikey':news_api_key,
    'qInTitle':company_name,
}


response=requests.get(stocks_endpoint,params=stocks_param)
data=response.json()['Time Series (Daily)']
data_list=[value for (key,value) in data.items()]
yesterday_close_price=data_list[0]['4. close']       # yesterday stock closing Price.

day_before_yesterday=data_list[1]['4. close']        # day before yesterday stck price.

difference=float(yesterday_close_price)-float(day_before_yesterday)

### it check the diffrence btween stock price
up_down=None
if difference>0:
    up_down='🔺'
else:
    up_down='🔻'
diff_percent=round((difference/float(yesterday_close_price))*100)


if abs(diff_percent<5):
    news_response=requests.get(news_endpoint,params=news_param)
    article=news_response.json()['articles'][:3]
    formated_article=[f"{company_name} {up_down}{diff_percent}\nHeadline : {item['title']}. \nBrief : {item['description']}" for item in article]
    client = Client(account_sid, auth_token)
    ## it helps to send msg
    for msg in formated_article:
        message = client.messages.create(body=msg,from_='+13158403254', to='+918700 810188')
        
