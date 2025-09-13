import requests
from twilio.rest import Client

account_sid = 'enter your account sid'
auth_token = 'enter your auth token'



Api_Key="enter your api_key"

parameter={
    'lat':28.709320,
    'lon':77.073959,
    'appid':Api_Key,
    'cnt':4
}

response=requests.get("https://api.openweathermap.org/data/2.5/forecast?",params=parameter)
weather_data=response.json()

is_rain=False
for weather in weather_data['list']:
    condition=weather['weather'][0]['id']
    if condition<700:
        is_rain=True
if is_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body='It is raining today. So please carry umbrella with you.',from_='+16315055475',to='+918700810188')
    print(message.sid)
