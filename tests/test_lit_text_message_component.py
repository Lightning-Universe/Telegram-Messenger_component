import os
from lit_text_message import TextMessage
import io
from contextlib import redirect_stdout


def test_send_message():
    twilio_sid = os.environ['TEST_TWILIO_SID']
    twilio_auth = os.environ['TEST_TWILIO_AUTH_TOKEN']
    twilio_phone = os.environ['TEST_TWILIO_PHONE_NUMBER']
    receiver_phone = os.environ['TEST_TWILIO_RECEIVER_PHONE_NUMBER']

    lit_text_message = TextMessage(
        twilio_phone=twilio_phone, 
        twilio_account_SID=twilio_sid,
        twilio_auth_token=twilio_auth
    )

    with io.StringIO() as buf, redirect_stdout(buf):
        lit_text_message.send_text('hi ⚡ from lightning ⚡', to=[receiver_phone])
        output = buf.getvalue()
        print(output)
        assert 'message id:' in output
