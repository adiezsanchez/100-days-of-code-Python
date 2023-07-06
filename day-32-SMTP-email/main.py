import datetime as dt
import random
import smtplib

now = dt.datetime.now()
my_email = "YOUR_SENDING_EMAIL"
to_email = "RECEIVING_EMAIL"
app_password = "PASSWORD"

if now.weekday() == 0:
    with open("./quotes.txt") as file:
        quote_list = [quote.strip() for quote in file.readlines()]
        today_quote = random.choice(quote_list)
        print(today_quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # Securing our connection to the e-mail server (encryption)
        connection.starttls()
        # Login:
        connection.login(user=my_email, password=app_password)
        # Sending mail
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:Monday Motivational quote (MMQ)\n\n{today_quote}."
        )
        # Once it reaches this point the connection is closed since we are using the "with" method.

# import datetime as dt
#
# # Create an object with "right now" properties and store it under a "now" variable:
# now = dt.datetime.now()
# # You can access some of its attributes
# year = now.year
# day_of_week = now.weekday()
# if year == 2022:
#     print("No need for facemask")
# print(year)
# print(day_of_week)
#
# # Create an object with "right now" properties and store it under a "now" variable:
# date_of_birth = dt.datetime(year=1989, month=12, day=2)
# print(f"This is my birthday: {date_of_birth}")
