from commands.command import Command
from fbchat import Message
from fbchat import Mention
import random


class choose(Command):

    def run(self):
        response_text = None
        if len(self.user_params) == 0:
            response_text = "@" + self.author.first_name + " Please enter something. Anything."
        else:
            try:
                if len(self.user_params) == 1:
                    response_text = "@" + self.author.first_name + " Your lucky number is {}"\
                        .format(random.randint(1, int(self.user_params[0])))
                elif len(self.user_params) == 2 and int(self.user_params[1]) > int(self.user_params[0]):
                    response_text = "@" + self.author.first_name + " Your lucky number is {}"\
                        .format(random.randint(int(self.user_params[0]), int(self.user_params[1])))
            except:
                pass
            if response_text is None:
                response_text = "@" + self.author.first_name + " Your lucky item is " + random.choice(self.user_params)

        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions= mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "ITEMS or NUMBERS",
            "function": "Picks a random ITEM out of the list or picks a random NUMBER from the specified range. How spooky."
        }