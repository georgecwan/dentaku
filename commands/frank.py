from commands.command import Command
from fbchat import Message

class frank(Command):
    def run(self):
        response_text = ""
        try:
            text = self.message_object.replied_to.text
            for i in text.split(" "):
                if len(i) > 1:
                    i = i[0] + i[2:]
                response_text += i + " "
        except AttributeError:
            try:
                for i in self.user_params:
                    i = i[0]+i[2:]
                    response_text += i+" "
            except:
                response_text = "*Indecipherable toxic junk*"
        except:
            response_text = "*Indecipherable toxic junk*"

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
