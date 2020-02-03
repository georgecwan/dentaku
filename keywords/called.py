from commands.command import Command
from fbchat import Message


class ass(Command):
    def run(self):
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
