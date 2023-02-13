import lightning as L

from lit_telegram import LitTelegram


class LitApp(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.lit_telegram_message = LitTelegram(
            telegram_token="171344532:AAHDVIBa1YBrywh4eiMwD-COyw", telegram_chat_id=-12345
        )

    def run(self):
        self.lit_telegram_message.send_text("hi ⚡ from lightning ⚡")


app = L.LightningApp(LitApp())
