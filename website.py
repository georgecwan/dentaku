from command import Command
from fbchat import Message
from fbchat import Mention


class website(Command):

    def run(self):
        response_text = "@" + self.author.first_name + "\nCheck our website out at https://vikingsdev.ca\n Events: " \
                                                       "vikingsdev.ca/events\n Workshops: vikingsdev.ca/workshops\n " \
                                                       "Sign Up: vikingsdev.ca/signup "
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions= mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )
