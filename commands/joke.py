from commands.command import Command
from fbchat import Message
import requests


class joke(Command):

    def run(self):
        url = "https://sv443.net/jokeapi/v2/joke/Any"
        json = requests.get(url).json()
        if 'joke' in json:
            response_text = json['joke']
        else:
            response_text = json['setup'] + "\n" + json['delivery']

        self.client.send(
            Message(text=response_text),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "None",
            "function": "Sends a random joke. May contain NSFW jokes."
        }
