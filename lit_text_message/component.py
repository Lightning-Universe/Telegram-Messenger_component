import lightning as L
from typing import List

from twilio.rest import Client


class TextMessage(L.LightningWork):
    def __init__(self, twilio_phone: str, twilio_account_SID: str, twilio_auth_token: str) -> None:
        """
        Sends a text (sms) message. Under the hood, it's powered by Twilio. You must
        visit Twilio to get an account id, auth token and phone number.

        1. Sign up here: https://www.twilio.com/try-twilio
        2. Visit this link to see all three items: https://console.twilio.com/

        Arguments:
            twilio_phone: a phone number you bought from twilio (ex: +14013150938)
            twilio_account_SID: the ID of your account
            twilio_auth_token: the token for your account

        """
        super().__init__()
        self.value = 0
        self.twilio_phone = twilio_phone
        self.twilio_account_SID = twilio_account_SID
        self.twilio_auth_token = twilio_auth_token

    def send_text(self, message: str, to: List[str], image_urls: List[str] = None):
        self.run('send_text', message, to, image_urls)

    def run(self, action, *args, **kwargs):
        if action == 'send_text':
            self._send_text(*args, **kwargs)
    
    def _send_text(self, message: str, to: List[str], image_urls: List[str] = None):
        client = Client(self.twilio_account_SID, self.twilio_auth_token)

        for phone in to:
            message = client.messages \
                .create(
                    body=message,
                    from_=self.twilio_phone,
                    media_url=image_urls,
                    to=phone
                )

            print('message sent! message id: ', message.sid)
