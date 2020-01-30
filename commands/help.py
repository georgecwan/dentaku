from commands.command import Command
from fbchat import Message
from fbchat import Mention
import os
import math
modules = [x for x in os.listdir("commands") if x.endswith(".py")]
modules = [x.replace(".py", "") for x in modules]
modules.sort()
# remove commands that are not for calling
modules.remove("command")
modules.remove("rate_limit")
modules.remove("__init__")


class help(Command):

    def get_instance(self, name):
        # returns an instance from the module 'name'
        module = __import__('commands.' + name, globals(), locals(), [name], 0)
        new_command = getattr(module, name)
        return new_command()

    def run(self):
        response_text = "@{}".format(self.author.first_name)
        if len(self.user_params) == 0:
            response_text += " Please signify if you would like to see part 1 or 2 of the commands list."
        elif len(self.user_params) == 1:
            try:
                # sends general information about all commands
                start = 0
                end = len(modules)
                if float(self.user_params[0]) == 1:
                    response_text += " Part 1/2"
                    end = math.ceil(len(modules) / 2)
                elif float(self.user_params[0]) == 2:
                    response_text += " Part 2/2"
                    start = math.ceil(len(modules) / 2)
                for x in modules[start:end]:
                    instance = self.get_instance(x)
                    response_text += "\n\n!" + x + ": " + instance.documentation["function"]
                response_text += "\n\nIf you want to learn more about a specific command, send '!help !COMMAND_NAME'."
            except:
                # sends detailed information about a specific command
                c_name = str(self.user_params[0]).replace("!", "", 1)
                if c_name in modules:
                    instance = self.get_instance(c_name)
                    response_text += """
                    \nThe !{} command:
                    \nFunction: {}
                    \nParameters: {}
                    """.format(c_name, instance.documentation["function"], instance.documentation["parameters"])
                else:
                    response_text += "\nlol good try"
        else:
            response_text += "\nSorry, we can only provide information on one command at a time!" \
                             + "\nPlease use the format: '!help !COMMAND_NAME'"
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "COMMAND_NAME / PART",
            "function": "Shows part of the general command options. Can show details about a specific COMMAND_NAME."
        }
