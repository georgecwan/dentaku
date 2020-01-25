from commands.command import Command
from fbchat.models import *
from fbchat import Mention
import bs4
import requests


class ud(Command):
    def run(self):
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
        try:
            link = "https://www.urbandictionary.com/define.php?term="
            for i in self.user_params:
                link += i+"+"
            link = link[:-1]
            req = requests.get(link)
            soup = bs4.BeautifulSoup(req.text, 'html.parser')
            response_text = "@" + self.author.first_name + "\n" + soup.find_all("div", class_="meaning")[0].get_text()
        except:
            response_text = "@" + self.author.first_name + " Your query was not valid or may not exit on UD. Please try again."
        self.client.send(
            Message(text=response_text, mentions=None),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "TERM",
            "function": "Searches for TERM with Urban Dictionary."
        }
