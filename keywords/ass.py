from commands.command import Command
from fbchat import Message
from fbchat import Mention
import string

class ass(Command):
    def run(self):
        msg = self.message_object.text.translate(str.maketrans('', '', string.punctuation)).lower()
        trigger = msg.find("ass")
        if self.client.uid != self.author_id and (trigger == 0 or msg[trigger-1] == " ")\
                and (trigger + 3 == len(msg) or msg[trigger+3] == " "):
            mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
            self.client.send(
                Message(text="@" + self.author.first_name + " I like ass.", mentions=mentions, reply_to_id=self.message_object.uid),
                thread_id=self.thread_id,
                thread_type=self.thread_type
            )

    def define_documentation(self):
        self.documentation = {
            "trigger": "ass",
            "function": "Likes ass."
        }
