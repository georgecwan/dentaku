from commands.command import Command
from fbchat import Message
import string

class called(Command):
    def run(self):
        msg = self.message_object.text.translate(str.maketrans('', '', string.punctuation)).lower()
        if "bot" in msg:
            trigger = msg.find("bot") + 3
        else:
            trigger = msg.find("dentaku") + 7
        if trigger == len(msg) or msg[trigger] == " ":
            if self.client.uid != self.author_id:
                self.client.send(
                    Message(text = "Someone called?"),
                    thread_id=self.thread_id,
                    thread_type=self.thread_type
                )

    def define_documentation(self):
        self.documentation = {
            "trigger": "bot",
            "function": "Bot is here."
        }
