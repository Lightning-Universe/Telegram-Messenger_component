import os
import io
import logging
from contextlib import redirect_stdout
from lit_telegram import LitTelegram

LOGGER = logging.getLogger(__name__)


def test_send_message(caplog):
    telegram_token = os.environ['TEST_TELEGRAM_TOKEN']
    telegram_chat_id = os.environ['TEST_TELEGRAM_CHAT_ID']

    lit_telegram_message = LitTelegram(
        telegram_token=telegram_token,
        telegram_chat_id=telegram_chat_id
    )

    msg = lit_telegram_message.send_text('hi ⚡ from lightning ⚡')
    output = buf.getvalue()
    assert 'message id:'  in caplog.text
