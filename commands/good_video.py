from commands.command import Command
from fbchat import Message
from fbchat import Mention


class good_video(Command):

    def run(self):
        response_text = "@" + self.author.first_name + "\nGood Videos Here:\nhttps://www.youtube.com/watch?v=3CQyYE1rMJg&t=6s\nhttps://www.youtube.com/watch?v=oHg5SJYRHA0\nhttps://www.youtube.com/watch?v=c5daGZ96QGU"
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "None",
            "function": "OMG I JUST SAW YOU IN THIS VIDEO!1!"
        }
