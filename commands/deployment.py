from commands.command import Command
from fbchat import Message
from fbchat import Mention
import time


class deployment(Command):

    def run(self):
        response_text = (
            "@{}"
            "\nI am currently on deployment #{}."
            "\nLast deployment was at {}").format(self.author.first_name, self.database['deployment'],
                                                  time.strftime('%Y-%m-%d %-I:%M %p',
                                                                time.localtime(self.database['last_deployment_time'])))
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "None",
            "function": "Gives deployment number and time."
        }
