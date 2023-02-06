# import smtplib
#
#
# my_email = "febrypythontest@gmail.com"
# password = "nbbhtyfjdjwqexzp"
# message = "cuman test"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,to_addrs="ebilma3@gmail.com",msg="Subject:Hello\n\nThis just testing")
#

# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# month = now.month
# weekday = now.weekday()
# birhtday = dt.datetime(year=1982,month=2,day=11)
# print(now)
# print(year)
# print(month)
# print(weekday)


import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()


my_email = "febrypythontest@gmail.com"
password = "nbbhtyfjdjwqexzp"
if weekday == 1 :
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="ebilma3@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{quote}")