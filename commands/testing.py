import json
from commands.command import Command
from fbchat import Message
from fbchat import Mention
import os

class testing(Command):

    def run(self):

        if not self.user_params:
            response_text = "@{} Test mode is currently {} which corresponds to \"{}\" in database.json. This means that the bot can{} accept group chat commands.".format(
                self.author.first_name, 'on' if self.database['testing'] == "y" else 'off', self.database['testing'],
                ' *not*' if self.database['testing'] == "y" else '')
        elif self.user_params[0].lower() == "on" or self.user_params[0].lower() == "off":
            if self.client.uid == self.author_id:
                self.database['testing'] = 'y' if self.user_params[0] == "on" else 'n'
                response_text = "@{} Test mode has been set to {}, which corresponds to \"{}\" in database.json.".format(
                    self.author.first_name, self.user_params[0], self.database['testing'])
            else:
                response_text = "@{} You do not have sufficient permissions to change this mode.".format(
                    self.author.first_name)
        with open("database.json", 'w') as outfile:
            json.dump(self.database, outfile)

        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "on/off",
            "function": "Turns off or on testing mode. Only the person who is running the bot can run this command. "
                        "With no paramemters, this command indicates whether testing mode is on or off. "
        }
