<!---:lai-name: Slack Messenger--->

<div align="center">
<img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/lai.png" width="200px">

A Lightning component to send a message on Telegram

______________________________________________________________________

[![Lightning](https://img.shields.io/badge/-Lightning-792ee5?logo=pytorchlightning&logoColor=white)](https://lightning.ai)
![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
![Tests](https://github.com/PyTorchLightning/LAI-telegram-messenger/actions/workflows/ci-testing.yml/badge.svg)

</div>

# About

This component lets you send a message on Telegram from a Lightning app.

______________________________________________________________________

## Use the component

<!---:lai-use:--->

```python
from lit_telegram import LitTelegram
import lightning as L


class LitApp(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.lit_telegram_message = LitTelegram(
            telegram_token="<YOUR_TELEGRAM_API_TOKEN>",
            telegram_chat_id="<YOUR_CHAT_ID>",
        )

    def run(self):
        self.lit_telegram_message.send_text("hi ⚡ from lightning ⚡")


app = L.LightningApp(LitApp())
```

## install

Use these instructions to install:

<!---:lai-install:--->

```bash
lightning install component lightning/LAI-telegram-messenger
```

Or to build locally

```bash
git clone https://github.com/PyTorchLightning/LAI-telegram-messenger
cd LAI-telegram-messenger
pip install -e .
```

## Tests

To run the test locally:

```bash
$ From the root of this package
pip install -r tests/requirements.txt
pytest
```

## Creating a Telegram account

1. Sign up here: https://web.telegram.org/?legacy=1#/login

1. Create new telegram bot using [BotFather](https://telegram.me/BotFather) and copy the api token.
   ![create bot](/images/botfather.png)

1. Obtain the chat id. Create a group invite `your_bot` and `Telegram Bot Raw` to obtain the chat id.
   ![enable 2-factor auth](/images/chat_id.png)
