# lit_telegram component
Use this component to send a text message in telegram.

## 1. Install lit telegram
First, install lit_telegram

```bash
lightning install component krishnakalyan3/lit-telegram
```

## 2. Create a telegram account
1. Sign up here: https://web.telegram.org/?legacy=1#/login

2. Create new telegram bot using [BotFather](https://telegram.me/BotFather) and copy the api token.
![create bot](/images/botfather.png)

3. Obtain the chat id. Create a group invite `your_bot` and `Telegram Bot Raw` to obtain the chat id.
![enable 2-factor auth](/images/chat_id.png)

## 3. Send message
To send a message, use lit-message in your app like this:

```python
from lit_telegram import LitTelegram
import lightning as L


class LitApp(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.lit_telegram_message = LitTelegram(
            telegram_token='171344532:AAHDVIBa1YBrywh4eiMwD-COyw', 
            telegram_chat_id=-12345
        )

    def run(self):
        self.lit_telegram_message.send_text('hi ⚡ from lightning ⚡')

app = L.LightningApp(LitApp())
```
