from commands.command import Command
from fbchat import Message
import requests
from random import choice


class news(Command):

    def run(self):
        if len(self.user_params) == 0:
            url = "https://newsapi.org/v2/top-headlines?language=en&apiKey=620bb40ce29b4ba6877ca164e3b9f008"
        elif self.user_params[0].lower() == "us":
            url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=620bb40ce29b4ba6877ca164e3b9f008"
        elif self.user_params[0].lower() == "canada" or self.user_params[0].lower() == "ca":
            url = "https://newsapi.org/v2/top-headlines?country=ca&apiKey=620bb40ce29b4ba6877ca164e3b9f008"
        else:
            url = "https://newsapi.org/v2/top-headlines?country={}&language=en&apiKey=620bb40ce29b4ba6877ca164e3b9f008"\
                .format(self.user_params[0].lower())
        try:
            json = requests.get(url).json()['articles']
            info = choice(json)
            response_text = "Here is your headline!\n"+info['title'] + "\n" + info['url']
        except:
            response_text = ("Unable to get news for your specified country. "
                             "To find the country of your choice please go to "
                             "https://newsapi.org/sources and enter the two letter "
                             "country code after !news. Sources may not be in English.")

        self.client.send(
            Message(text=response_text),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "None/Canada/US",
            "function": "Get a random recent headline."
        }
