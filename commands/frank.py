from commands.command import Command
from fbchat import Message
from random import randint


class frank(Command):
    def run(self):
        response_text = ""
        if len(self.user_params) == 0 and self.message_object.replied_to == None:
            response_text = " *Indecipherable toxic junk* "
        try:
            text = self.message_object.replied_to.text
            for i in text.split(" "):
                if len(i) > 1:
                    count = 0
                    while count < len(i)/5:
                        rand = randint(1, len(i))
                        i = i[:rand] + i[rand+1:]
                        count += 1
                response_text += i + " "
        except AttributeError:
            try:
                for i in self.user_params:
                    i = i[0]+i[2:]
                    response_text += i+" "
            except:
                response_text = "Something's not right. I can feel it."
        except:
            response_text = "Everything is going badly and I don't know why."

        self.client.send(
            Message(text=response_text, mentions=None),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "REPLIED_MESSAGE",
            "function": "frank-ify a REPLIED_MESSAGE"
        }
