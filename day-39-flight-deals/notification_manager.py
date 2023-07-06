from twilio.rest import Client

TWILIO_SID = 'TWILIO_SID '
TWILIO_AUTH_TOKEN = 'TWILIO_AUTH_TOKEN'

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_='TWILIO_NR',
            to='YOUR_PHONE_NUMBER',
        )
        # Prints if successfully sent.
        print(message.sid)
        print(message.status)

    def send_whatsapp(self, message):
        message = self.client.messages.create(
            body=message,
            from_='whatsapp:TWILIO_NR',
            to='whatsapp:YOUR_PHONE_NUMBER',
        )
        # Prints if successfully sent.
        print(message.sid)
        print(message.status)
