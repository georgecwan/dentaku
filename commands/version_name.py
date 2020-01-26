from commands.command import Command
from fbchat import Message
from fbchat import Mention
import requests
import json
import random

class version_name(Command):

    def run(self):
        person = json.loads(requests.get("https://anfi.tk/greekApi/person/random").text)["name"]
        alliterations: list = json.loads(requests.get("https://api.datamuse.com/words?sp={}*&md=p".format(person[0])).text)
        for word in alliterations:
            print(word)
            if "tags" not in word or "adj" not in word['tags']:
                alliterations.remove(word)
        adjective: str = random.choice(alliterations)["word"]
        adjective = adjective.capitalize()
        response_text = (
            "@{}"
            " {} {}").format(self.author.first_name, adjective, person)
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "None",
            "function": "More information on the vikingsDev website!"
        }
