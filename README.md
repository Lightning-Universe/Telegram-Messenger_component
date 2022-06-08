<!---:lai-name: Slack Messenger--->

<div align="center">
<img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/lai.png" width="200px">

A Lightning component to send a message on Slack
______________________________________________________________________

</div>

# About
This component lets you send a message on Slack from a Lightning app.

----

## Use the component

<!---:lai-use:--->
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

## install
Use these instructions to install:

<!---:lai-install:--->
```bash
git clone https://github.com/PyTorchLightning/LAI-telegram-messenger
cd LAI-telegram-messenger
pip install -r requirements.txt
pip install -e .
```


## Creating a Telegram account
1. Sign up here: https://web.telegram.org/?legacy=1#/login

2. Create new telegram bot using [BotFather](https://telegram.me/BotFather) and copy the api token.
![create bot](/images/botfather.png)

3. Obtain the chat id. Create a group invite `your_bot` and `Telegram Bot Raw` to obtain the chat id.
![enable 2-factor auth](/images/chat_id.png)
