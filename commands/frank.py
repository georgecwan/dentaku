from commands.command import Command
from fbchat import Message
from random import randint


class frank(Command):
    def run(self):
        response_text = ""
        if self.message_object.replied_to is not None:
            text = self.message_object.replied_to.text.split(" ")
        elif len(self.user_params) > 0:
            text = self.user_params
        else:
            text = ""
            response_text = " *Indecipherable toxic junk*"
        for i in text:
            if len(i) > 1:
                count = 0
                while count < len(i) / 5:
                    rand = randint(0, len(i))
                    i = i[:rand] + i[rand + 1:]
                    count += 1
            response_text += i + " "

        self.client.send(
            Message(text=response_text),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "REPLIED_MESSAGE",
            "function": "frank-ify a REPLIED_MESSAGE"
        }
