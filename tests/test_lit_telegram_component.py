import os
import io
import logging
from lit_telegram import LitTelegram


def test_send_message(caplog):
    caplog.set_level(logging.INFO)
    logger = logging.getLogger('app')
    logger.propagate = True  
    
    telegram_token = os.environ['TEST_TELEGRAM_TOKEN']
    telegram_chat_id = os.environ['TEST_TELEGRAM_CHAT_ID']

    lit_telegram_message = LitTelegram(
        telegram_token=telegram_token,
        telegram_chat_id=telegram_chat_id
    )

    msg = lit_telegram_message.send_text('hi ⚡ from lightning ⚡')
    assert 'message id:'  in caplog.text
