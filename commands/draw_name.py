from commands.command import Command
from fbchat import Message
from fbchat import Mention
from random import randint

class draw_name(Command):

    def run(self):
        if len(self.user_params) == 0:
            response_text = "@" + self.author.first_name + " Please enter something. Anything"
        else:
            try:
                if len(self.user_params) == 1:
                    response_text = "@" + self.author.first_name + " Your lucky number is " + str(randint(1, float(self.user_params[0])))
                elif len(self.user_params) == 2 and float(self.user_params[1]) > float(self.user_params[0]):
                    response_text = "@" + self.author.first_name + " Your lucky number is " + str(randint(float(self.user_params[0]), float(self.user_params[1])))
                else:
                    draw = randint(0, len(self.user_params) - 1)
                    response_text = "@" + self.author.first_name + " Your lucky item is " + self.user_params[draw]
            except:
                draw = randint(0, len(self.user_params) - 1)
                response_text = "@" + self.author.first_name + " Your lucky item is " + self.user_params[draw]

        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions= mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "NAMES or NUMBER",
            "function": "Picks a random name out of the list or picks a random number. How spooky."
        }