from commands.command import Command
from fbchat import Message
from fbchat import Mention


class ass(Command):
    def run(self):
        if self.client.uid != self.author_id:
            mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
            self.client.send(
                Message(text="@" + self.author.first_name + " I like ass.", mentions=mentions),
                thread_id=self.thread_id,
                thread_type=self.thread_type
            )

    def define_documentation(self):
        self.documentation = {
            "trigger": "ass",
            "function": "Likes ass."
        }
