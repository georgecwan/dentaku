from commands.command import Command
from fbchat import Message
import requests


class trump(Command):

    def run(self):
        url = "https://www.tronalddump.io/random/quote"
        json = requests.get(url).json()
        response_text = json['appeared_at'][:10]+"\n"+json['value']+"\n"+json['_embedded']['source'][0]['url']

        self.client.send(
            Message(text=response_text),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "None",
            "function": "What is Trump thinking?"
        }
