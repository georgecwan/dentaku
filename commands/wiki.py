from commands.command import Command
from fbchat import Message
from fbchat import Mention
import bs4
import requests

class wiki(Command):

    def run(self):
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
        if len(self.user_params) == 0:
            response_text = "@" + self.author.first_name + " Here you go." + "\n" + "https://en.wikipedia.org/wiki/Nothing"
        else:
            try:
                link = "https://en.wikipedia.org/w/index.php?search="+"_".join(self.user_params)
                webpage = requests.get(link)
                text = str(bs4.BeautifulSoup(webpage.text, 'html.parser').find("div", class_="mw-search-result-heading"))
                if text == "None":
                    link = webpage.url
                else:
                    text = text[text.find("href") + 6:]
                    text = text[:text.find("\"")]
                    link = "https://en.wikipedia.org" + text
                response_text = "@" + self.author.first_name + " Here's what I found for you about " + " ".join(self.user_params) \
                                + ": " + link
            except:
                response_text = "@" + self.author.first_name + " Wikipedia cannot get a result."

        self.client.send(
            Message(text=response_text, mentions= mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "SEARCH_TERM",
            "function": "Looks for a Wikipedia article with SEARCH_TERM to quench your thirst for knowledge."
        }