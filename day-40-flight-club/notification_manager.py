from twilio.rest import Client
import smtplib

TWILIO_SID = 'TWILIO_SID'
TWILIO_AUTH_TOKEN = 'TWILIO_AUTH_TOKEN'
my_email = "YOUR_EMAIL"
to_email = "TO_EMAIL"
app_password = "APP_PASSWORD"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_='+TWILIO_PHONE',
            to='+YOUR_PHONE',
        )
        # Prints if successfully sent.
        print(message.sid)
        print(message.status)

    def send_whatsapp(self, message):
        message = self.client.messages.create(
            body=message,
            from_='whatsapp:+TWILIO_PHONE',
            to='whatsapp:+YOUR_PHONE',
        )
        # Prints if successfully sent.
        print(message.sid)
        print(message.status)

    def send_email(self, message, google_flight_link, emails):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # Securing our connection to the e-mail server (encryption)
            connection.starttls()
            # Login:
            connection.login(user=my_email, password=app_password)
            # Sending mail
            for to_email in emails:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=to_email,
                    msg=f"Subject:Low Price Flight Alert\n\n{message}\n{google_flight_link}".encode('utf-8')
            )
            # Once it reaches this point the connection is closed since we are using the "with" method.
