from command import Command
from fbchat import Message
from fbchat import Mention


class help(Command):

    def run(self):
        response_text = "@" + self.author.first_name + "!Website: Website Info"
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions= mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )
