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
