from commands.command import Command
from fbchat import Message
from fbchat import Mention
import requests


class fortune(Command):

    def run(self):
        response_text = "@" + self.author.first_name
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
        url = "https://helloacm.com/api/fortune/"
        try:
            response_text += " " + requests.get(url).json()
        except:
            pass
        if response_text == "@" + self.author.first_name:
            response_text += " Fortune unavailable"

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "None",
            "function": "Gives you a random fortune."
        }
