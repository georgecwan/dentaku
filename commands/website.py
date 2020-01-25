from commands.command import Command
from fbchat import Message
from fbchat import Mention


class website(Command):

    def run(self):
        response_text = """
        @{}
        \nCheck out our website out at https://vikingsdev.ca
        \nEvents: vikingsdev.ca/events
        \nWorkshops: vikingsdev.ca/workshops
        \nSign Up: vikingsdev.ca/signup
        """.format(self.author.first_name)
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "None",
            "function": "More information on the vikingsDev website!"
        }
