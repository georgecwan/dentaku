from commands.command import Command
from fbchat import Message
import requests


class advice(Command):

    def run(self):
        url = "https://api.adviceslip.com/advice"
        json = requests.get(url).json()
        response_text = json['slip']['advice']

        self.client.send(
            Message(text=response_text),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "None",
            "function": "Get some free advice!"
        }
