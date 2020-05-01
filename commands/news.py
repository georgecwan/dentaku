from commands.command import Command
from fbchat import Message
import requests
from random import randint


class news(Command):

    def run(self):
        if len(self.user_params) > 0 and self.user_params[0].lower() == "us":
            url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=620bb40ce29b4ba6877ca164e3b9f008"
        else:
            url = "https://newsapi.org/v2/top-headlines?country=ca&apiKey=620bb40ce29b4ba6877ca164e3b9f008"
        json = requests.get(url).json()['articles']
        num = randint(0, len(json) - 1)
        info = json[num]
        response_text = "Here is your headline!\n"+info['title'] + "\n" + info['url']

        self.client.send(
            Message(text=response_text),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "None(Canada)/US",
            "function": "What is Trump thinking?"
        }
