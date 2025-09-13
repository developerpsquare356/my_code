
######################    Amazon Price tracker Project    ####################################################################################################

import requests
import smtplib
from bs4 import BeautifulSoup

#==============   smtp details of email  =================================

my_mail="enter your email"
my_password="enter your password "

#=========================   Basic URL Needed in this Project

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


#==============================    main.py   =================================

response=requests.get(live_url,headers=header)

soup=BeautifulSoup(response.content,"html.parser")

data=soup.find(class_='aok-offscreen').getText()
price=float(data.split()[0].split("$")[1])

content=soup.find(class_="a-size-large product-title-word-break").getText()
msg=''
for i in content.split():
    msg=msg+i+' '


#===============      SMTP Code For Project    ===========================
BUY_PRICE = float(100)

if price < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connect:
        connect.starttls()
        connect.login(user=my_mail,password=my_password)
        connect.sendmail(
            from_addr=my_mail,
            to_addrs="receiver email",
            msg=f'{msg} \n Now this product is available at $ {price}'.encode("utf-8")
        )

