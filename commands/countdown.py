from commands.command import Command
from fbchat import Message
from fbchat import Mention


class countdown(Command):

    def run(self):
        try:
            count = int(self.user_params[0])
            if count > 10:
                response_text = "I'm too lazy to do that..."
            elif count <= 0:
                response_text = "Lets do it again!"
            else:
                response_text = "!countdown " + str(count - 1)
            mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
        except ValueError:
            response_text = "You think you're soooo clever? Not anymore " + self.author.first_name + ", because I now have error catching!"
        self.client.send(
            Message(text=response_text),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "NUMBER",
            "function": "Counts down recursively from NUMBER."
        }
