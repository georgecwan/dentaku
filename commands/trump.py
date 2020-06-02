from commands.command import Command
from fbchat import Message
import requests


class trump(Command):

    def run(self):
        response_text = "Trump thinks that: "
        url = "https://api.whatdoestrumpthink.com/api/v1/quotes/random"
        json = requests.get(url).json()
        response_text += json['message']

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
