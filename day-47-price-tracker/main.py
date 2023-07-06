import smtplib
import requests
from bs4 import BeautifulSoup

# URL INFO
URL="https://www.amazon.com/Sony-WH-1000XM5-Canceling-Headphones-Hands-Free/dp/B09XS7JWHH?th=1"
HEADERS = {
    "Accept-Language":"es-ES,es;q=0.9,en;q=0.8,ca;q=0.7,no;q=0.6",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
# EMAIL-CRED
my_email = "YOUR_EMAIL"
to_email = "TO_EMAIL"
app_password = "app_password"

#Store the html response
response = requests.get(URL, headers=HEADERS)
#Transform the response into a beautiful soup object
soup = BeautifulSoup(response.text, "lxml")
#Look for the price span tag element
price_span_tag = soup.find(name="span", class_="a-offscreen")
#Get the string value and split the dollar sign and the price into a 2 element list
price = price_span_tag.getText().split("$")
#Choose the price from the list and transform type str into float number
price_float = float(price[1])

if price_float < 400:
    print("send_email")
    mail_content = f"You can buy it now at: ${price_float} at {URL}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # Securing our connection to the e-mail server (encryption)
        connection.starttls()
        # Login:
        connection.login(user=my_email, password=app_password)
        # Sending mail
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:Price Alert on {soup.title.getText()}\n\n{mail_content}."
        )
        # Once it reaches this point the connection is closed since we are using the "with" method.
