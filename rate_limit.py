from command import Command
from fbchat import Message
from fbchat import Mention
import requests
import json

class rate_limit(Command):
    def run(self):
        response = json.loads(requests.get("https://api.github.com/rate_limit").text)
        remaining = response['rate']['remaining']
        response_text = """
        @{}\nRemaining pings: {}
        """.format(self.author.first_name, remaining)
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions= mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )
