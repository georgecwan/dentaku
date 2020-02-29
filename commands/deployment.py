from commands.command import Command
from fbchat import Message
from fbchat import Mention
import time
import requests


class deployment(Command):

    def run(self):
        try:
            next_deployment = requests.get("http://0.0.0.0:1088/next")
            next_deployment = next_deployment.json()["next_check"]
            next_deployment = time.strftime('%Y-%m-%d %-I:%M %p', time.localtime(next_deployment))
        except:
            next_deployment = "Unable to get next deployment time."

        last_deployment = time.strftime('%Y-%m-%d %-I:%M %p', time.localtime(self.database['last_deployment_time']))

        response_text = (
            "@{}"
            "\nI am currently on deployment #{}."
            "\nLast deployment was at {}"
            "\nNext deployment is at {}").format(self.author.first_name, self.database['deployment'], last_deployment, next_deployment)

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
