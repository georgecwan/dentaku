from commands.command import Command
from fbchat import Message
import requests
from bs4 import BeautifulSoup


class wiki(Command):

    def run(self):
        link = "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&prop=info&inprop=url&format=json".format(
            "%20".join(self.user_params))
        result = requests.get(link).json()['query']['search'][0]
        response_text = result['title'] + ":\n" + BeautifulSoup(result['snippet'], features="html.parser").text + "..."
        response_text += "\n\nhttps://en.wikipedia.org/?curid={}".format(result['pageid'])

        self.client.send(
            Message(text=response_text),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "SEARCH_TERM",
            "function": "Looks for a Wikipedia article with SEARCH_TERM to quench your thirst for knowledge."
        }