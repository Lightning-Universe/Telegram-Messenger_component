import logging

import lightning as L
from telegram import Bot


class LitTelegram(L.LightningFlow):
    def __init__(self, telegram_token: str, telegram_chat_id: int) -> None:
        """Sends a text message in Telegram. You must have a telegram account to get telegram_token and
        telegram_chat_id.

        Arguments:
            telegram_token: API token obtained using BotFather
            telegram_chat_id: Chat ID obtained using Telegram Bot Raw
        """
        super().__init__()
        self.telegram_token = telegram_token
        self.telegram_chat_id = telegram_chat_id

    def send_text(self, message: str):
        self.run("send_text", message)

    def run(self, action, *args, **kwargs):
        if action == "send_text":
            self._send_text(*args, **kwargs)

    def _send_text(self, message: str):
        telegram_client = Bot(token=self.telegram_token)
        message = telegram_client.sendMessage(chat_id=self.telegram_chat_id, text=message)
        logging.info(f"message sent! message id: {message.message_id}")
