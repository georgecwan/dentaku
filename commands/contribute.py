from commands.command import Command
from fbchat import Message
from fbchat import Mention


class contribute(Command):

    def run(self):
        response_text = """
        @{} 
        \nYou can contribute to Dentaku here: https://github.com/VikingsDev/Dentaku
        \nFor more information, check out vikingsDev Bounties: https://vikingsdev.ca/bounties
        \nHappy contributing!
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
            "function": "Learn how to become a bounty hunter."
        }
