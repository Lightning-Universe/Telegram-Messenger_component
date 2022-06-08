import os
from lit_telegram import LitTelegram
import io
from contextlib import redirect_stdout


def test_send_message():
    #telegram_token = os.environ['TEST_TELEGRAM_TOKEN']
    #telegram_chatid = os.environ['TEST_TELEGRAM_CHAT_ID']
    telegram_token = "1713459832:AAHDVIBa1YBrywh4eiMwD-CO8B0dDMetgyw"
    telegram_chatid = -644398766

    lit_telegram_message = LitTelegram(
        telegram_token=telegram_token, 
        telegram_chat_id=telegram_chat_id
    )

    with io.StringIO() as buf, redirect_stdout(buf):
        lit_telegram_message.send_text('hi ⚡ from lightning ⚡')
        output = buf.getvalue()
        print(output)
