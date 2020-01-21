from command import Command
from fbchat import Message
from fbchat import Mention


class help(Command):
    def run(self):
        response_text = """
        @{}
        \n!website: Website Info
        \n!help: Shows list of commands
        \n!good_video: List of videos.
        \n!countdown [num]: Counts down from num. 
        \n!contribute: Learn how to be a bounty hunter.
        \n!a_chance_at_uni: All your hopes and dreams come true!
        """.format(self.author.first_name)
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions= mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )
