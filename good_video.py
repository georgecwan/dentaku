from command import Command
from fbchat import Message
from fbchat import Mention


class good_video(Command):

    def run(self):
        response_text = "@" + self.author.first_name + "Good Video Here:\nhttps://www.youtube.com/watch?v=3CQyYE1rMJg&t=6s"
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions= mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )
