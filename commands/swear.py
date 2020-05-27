from commands.command import Command
from fbchat import Message


class swear(Command):

    def run(self):
        if len(self.user_params) > 0 and self.user_params[0].lower() == "reset":
            self.thread_data['swears'] = {}
            response_text = "The swear counter has been reset."
        elif 'swears' in self.thread_data and len(self.thread_data['swears']) > 0:
            response_text = "Swear Counter:"
            for id, count in self.thread_data['swears'].items():
                response_text += "\n{}: {}".format(self.getName(id), count)
        else:
            response_text = "Not enough people swore."

        self.client.send(
            Message(text=response_text),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "None / 'reset'",
            "function": "Prints the swear rankings."
        }