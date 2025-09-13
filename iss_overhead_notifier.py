
##                   Match sunset time with current time

import requests
from datetime import datetime
import smtplib
import time

my_mail="developerpsquare356@gmail.com"
my_password="yrjpodwmivurrvls"

my_latitude=20.593683
my_longitude=78.962883

def Is_iss_overhead():
    response=requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()
    iss_lat=data['iss_position']["latitude"]
    iss_lng=data['iss_position']["longitude"]

    if my_latitude-5<=iss_lat<=my_latitude+5 and my_longitude-5<=iss_lat<=my_longitude+5:
        return True

def is_night():
    parameter = {
        "lat": my_latitude, "lng": my_longitude, "formated": 0
    }

    sun_API=requests.get("https://api.sunrise-sunset.org/json",parameter)
    sun_API.raise_for_status()
    info=sun_API.json()
    sunrise=int (info["results"]['sunrise'].split("T")[1].split[":"][0])
    sunset=int (info["results"]['sunset'].split("T")[1].split[":"][0])

    time_now=datetime.now().hour
    if time_now>=sunset or time_now<=sunrise:
        return True

while True:
    time.sleep(60)
    if Is_iss_overhead() and is_night():
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_mail, password=my_password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs="prantikpal.399@gmail.com",
            msg=f'Subject:Birthday Wishes\n\n hello soja jake')
