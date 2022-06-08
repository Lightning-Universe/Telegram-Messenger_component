# lit_text_message component
Use this component to send a text message (powered by Twilio).


## 1. Install lit message 
First, install lit_text_message 

```bash
lightning install component lightning/lit-message
```

## 2. Create a twilio account
1. Sign up here: https://www.twilio.com/try-twilio
2. Visit this link to see all three items: https://console.twilio.com/

You're going to need all 3 of these items:
![twilio creds](/images/twilio.jpg)

## 3. Send message
To send a message, use lit-message in your app like this:

```python
from lit_text_message import TextMessage

import lightning as L

class LitApp(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.lit_text_message = TextMessage(
            twilio_phone='+11112223344', 
            twilio_account_SID='AC03d87f75da114c000e38437bb2736148', 
            twilio_auth_token='4a53b0455e40706e4e1909fe8ff81a2f'
        )

    def run(self):
        self.lit_text_message.send_text('hi ⚡ from lightning ⚡', to=['+1999887766'])

app = L.LightningApp(LitApp())
```
