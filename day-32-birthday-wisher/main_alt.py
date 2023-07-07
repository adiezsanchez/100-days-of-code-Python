##################### Normal Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib

my_email = "YOUR_EMAIL"
app_password = "YOUR_APP_PASSWORD"

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
now = dt.datetime.now()
today_month = now.month
today_day = now.day
today_tuple = (today_month, today_day)

# HINT 2: Use pandas to read the birthdays.csv
df = pd.read_csv("./birthdays.csv")
# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in df.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    name = birthday_person["name"]
    to_email = birthday_person["email"]
# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
        contents = letter.read()
    with open("./new_letter.txt", mode="w") as n_letter:
        n_letter.write(contents.replace("[NAME]", name))
    with open("./new_letter.txt") as n_letter:
        n_letter_content = n_letter.read()
# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.
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

