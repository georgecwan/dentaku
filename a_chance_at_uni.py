from command import Command
from fbchat import Message
from fbchat import Mention

class a_chance_at_uni(Command):

    def run(self):
        if len(self.user_params) > 0:
            response_text = "@" + self.author.first_name + "\n u op guaranteed acceptance at " + self.user_params[0]
        else:
            response_text = "@" + self.author.first_name + "\n u op guaranteed acceptance at HYPSM"
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )
