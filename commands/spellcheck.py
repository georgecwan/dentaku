from commands.command import Command
from fbchat import Message
from fbchat import Mention
import bs4
import requests
import string

class spellcheck(Command):

    def run(self):
        if len(self.user_params) == 0 and self.message_object.replied_to == None:
            response_text = "@" + self.author.first_name + " An empty sentence has no mistakes."
        else:
            link = "http://www.openbookproject.net/courses/python4fun/_static/spellcheck/spell.words"
            webpage = requests.get(link)
            text = str(bs4.BeautifulSoup(webpage.text, 'html.parser').getText())
            try:
                msg = self.message_object.replied_to.text.translate(str.maketrans('', '', string.punctuation))
                mis = ""
                for i in msg.split(" "):
                    if "\n"+i.lower()+"\n" not in text and i.lower() != "a" and i.lower() != "zymin":
                        mis += " " + i
                if mis != "":
                    response_text = "@" + self.author.first_name + " Mispelled words:" + mis
                else:
                    response_text = "@" + self.author.first_name + " Seems legit"
            except AttributeError:
                #try:
                    mis = ""
                    for i in self.user_params:
                        if "\n" + i.translate(str.maketrans('', '', string.punctuation)).lower() + "\n" not in text and i.lower() != "a" and i.lower() != "zymin":
                            mis += " " + i
                    if mis != "":
                        response_text = "@" + self.author.first_name + " Mispelled words:" + mis
                    else:
                        response_text = "@" + self.author.first_name + " Seems legit"
                #except:
                    #response_text = "@" + self.author.first_name + " Dude I can't even read your sentence."
            except:
                response_text = "@" + self.author.first_name + " Dude I can't even read your sentence."

        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions= mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "REPLIED_MESSAGE",
            "function": "Checks the spelling in REPLIED_MESSAGE for real words."
        }