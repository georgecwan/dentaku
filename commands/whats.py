from commands.command import Command
from fbchat.models import *

whatarray = {
'bofa': 'bofA deez nUts',
'ligma': 'ligma b a l l s',
'rhydon': 'rhydon dis DICK',
'sugandese': 'sug an deez balls',
'updog': 'whats up dog <3 wanna get sum tonight no homo',
'imagine dragons': 'imagine me dragon deez nuts all over ur face',
'candice': 'candice dick fit in yo mouf',
'parody': 'u can get a parodyz bahls',
'sugma': 'i feel stupid coding this manually and i really want to stop'
}

class whats(Command):
    def run(self):
        whats = " ".join(self.user_params)
        try:
            response_text = whatarray[whats]
        except KeyError:
            response_text = "I cannot perform this request because your dick is too big and has proposed a ligma joke that has not been coded."
        self.client.send(
            Message(text=response_text, mentions=None),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "JOKE_STARTER",
            "function": "Try sending a JOKE_STARTER."
        }
