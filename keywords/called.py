from commands.command import Command
from fbchat import Message
import string

class called(Command):
    def run(self):
        msg = self.message_object.text.translate(str.maketrans('', '', string.punctuation)).lower()
        if (" {} ").format(msg).find(" dentaku ") >= 0 and self.client.uid != self.author_id:
            self.client.send(
                Message(text="Someone called?"),
                thread_id=self.thread_id,
                thread_type=self.thread_type
            )

    def define_documentation(self):
        self.documentation = {
            "trigger": "Dentaku",
            "function": "I am Dentaku."
        }
