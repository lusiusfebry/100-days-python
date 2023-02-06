from twilio.rest import Client

TWILIO_SID = "AC92f5da339cd2c9077843d36afec55a29"
TWILIO_AUTH_TOKEN = "b606e2db1eff1427f99899f4216c2df6"
TWILIO_VIRTUAL_NUMBER = "+13149475427"
TWILIO_VERIFIED_NUMBER = "+6285696109319"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)