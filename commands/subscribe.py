import json

from commands.command import Command
from fbchat import Message
from fbchat import Mention
import os


class subscribe(Command):

    def run(self):
        if os.path.exists("database.json"):
            with open("database.json", 'r') as file:
                database = json.load(file)
        else:
            database = {}
            database['subscription'] = []

        if not self.user_params:
            if self.author_id in database['subscription']:
                response_text = """
                                   @{} You were already subscribed!
                                   """.format(self.author.first_name)
            else:
                database['subscription'].append(self.author_id)
                response_text = """
                               @{} You have been subscribed to deployment notifications!
                               """.format(self.author.first_name)
        elif self.user_params[0] == 'remove':
            if self.author_id in database['subscription']:
                database['subscription'].remove(self.author_id)
                response_text = """
                               @{} You have been unsubscribed from deployment notifications!
                               """.format(self.author.first_name)
            else:
                response_text = """
                               @{} No action taken. You are currently not subscribed to deployments.
                               """.format(self.author.first_name)


        with open("database.json", 'w') as outfile:
            json.dump(database, outfile)

        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "remove",
            "function": "Subscribes a user to Dentaku updates. Removes user if parameter remove is present."
        }
