import datetime as dt
import random
import pandas as pd
import smtplib

now = dt.datetime.now()
day = now.day
month = now.month

my_email = "adiez.biotech@gmail.com"
app_password = "sghs klth krtj dued"

with open("./birthdays.csv") as file:
    birthdays = pd.read_csv(file)
    birthdays_dict_list = birthdays.to_dict(orient="records")

for persons in birthdays_dict_list:
    if persons["day"] == day and persons["month"] == month:
        name = persons["name"]
        to_email = persons["email"]
        print(f"Today is {name}'s birthday, and this is its e-mail {to_email}")

        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            contents = letter.read()
        with open("./new_letter.txt", mode="w") as n_letter:
            n_letter.write(contents.replace("[NAME]", name))
        with open("./new_letter.txt") as n_letter:
            n_letter_content = n_letter.read()
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # Securing our connection to the e-mail server (encryption)
            connection.starttls()
            # Login:
            connection.login(user=my_email, password=app_password)
            # Sending mail
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject:Happy Birthday\n\n{n_letter_content}."
            )
            # Once it reaches this point the connection is closed since we are using the "with" method.




