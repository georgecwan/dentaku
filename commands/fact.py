from commands.command import Command
from fbchat import Message
from urllib.request import urlopen
import json


class fact(Command):

    def run(self):
        url = "https://uselessfacts.jsph.pl/random.json?language=en"
        jsonurl = urlopen(url)
        info = json.loads(jsonurl.read())
        response_text = "FACT: "+info['text']

        self.client.send(
            Message(text=response_text),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "None",
            "function": "Gives you a random fact."
        }
