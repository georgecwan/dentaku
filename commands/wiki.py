from commands.command import Command
from fbchat import Message
from fbchat import Mention
import bs4
import requests

class wiki(Command):

    def run(self):
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
        resultfound = False
        try:
            link = "https://wikipedia.org/w/index.php?search="+"_".join(self.user_params)
            webpage = requests.get(link)
            text = str(bs4.BeautifulSoup(webpage.text, 'html.parser').find("div", class_="mw-search-result-heading"))
            if text == None:
                link = webpage.url
            else:
                text = text[text.find("href") + 6:]
                text = text[:text.find("\"")]
                link = "https://wikipedia.org"+text
            response_text = "@" + self.author.first_name + " Here's what I found for you on " + " ".join(self.user_params)
            resultfound = True
        except:
            response_text = "@" + self.author.first_name + " Wikipedia cannot get a result."

        self.client.send(
            Message(text=response_text, mentions= mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

        if resultfound == True:
            self.send_link(self, link)

    def define_documentation(self):
        self.documentation = {
            "parameters": "SEARCH TERMS",
            "function": "Gives you the link to a Wikipedia article to satisfy your thirst for knowledge."
        }

    def send_link(self, link):
        self.client.send(
            Message(text=link),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )