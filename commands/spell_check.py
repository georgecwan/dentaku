from commands.command import Command
from fbchat import Message
from fbchat import Mention
import requests
import string


class spell_check(Command):

    def checkWord(self, word):
        url = "https://wordsapiv1.p.rapidapi.com/words/{}".format(word)
        headers = {
            "X-Mashape-Key": "8bef51c08bmsh96dc3702341e39ep14a15bjsn19a83064d62d",
            "Accept": "application/json"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 404:
            return False
        return True

    def run(self):
        response_text = "@" + self.author.first_name
        if len(self.user_params) == 0 and self.message_object.replied_to == None:
            response_text += " An empty sentence has no mistakes."
        elif self.message_object.replied_to is not None:
            msg = self.message_object.replied_to.text.translate(str.maketrans('', '', string.punctuation))
            mis = ""
            for word in msg.split(" "):
                if not self.checkWord(word):
                    mis += " " + word
            if len(mis) > 0:
                response_text += " Misspelled words:" + mis
            else:
                response_text += " Seems legit"
        else:
            '''
            link = "http://www.openbookproject.net/courses/python4fun/_static/spellcheck/spell.words"
            webpage = requests.get(link)
            text = str(bs4.BeautifulSoup(webpage.text, 'html.parser').getText())
            '''
            mis = ""
            for i in self.user_params:
                if not self.checkWord(i.translate(str.maketrans('', '', string.punctuation))):
                    mis += " " + i
            if len(mis) > 0:
                response_text += " Misspelled words:" + mis
            else:
                response_text += " Seems legit"

        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "REPLIED_MESSAGE",
            "function": "Checks the spelling in REPLIED_MESSAGE."
        }
