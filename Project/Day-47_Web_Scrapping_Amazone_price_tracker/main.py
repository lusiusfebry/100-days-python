from bs4 import BeautifulSoup
import requests
import smtplib
import lxml
import html
import os
URL = "https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=sr_1_1?crid=1VL8U25B9X3TF"

my_email = "febrypythontest@gmail.com"
my_password = os.getenv("password_email")
to_email = "lusiusfebry@gmail.com"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9,id;q=0.8"
}

response = requests.get(url=URL,headers=headers)
soup = BeautifulSoup(response.text,"lxml")

product_title = soup.find("span",{"id":"productTitle"}).get_text().strip().encode('utf-8','xmlcharrefreplace')
# print(product_title)
# print(html.unescape(product_title))
price = soup.find("span",class_="a-price-whole").text
decimal_price = soup.find("span",class_="a-price-fraction").text
current_price = float(price+decimal_price)

target_price = 500

message = f"Subject: New Alert from Amazon\n\n{product_title} is now {current_price} \nlink {URL}"
print(message)
if current_price < target_price:


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=message)


