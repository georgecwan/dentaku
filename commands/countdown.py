from commands.command import Command
from fbchat import Message
from fbchat import Mention


class countdown(Command):

    def run(self):
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
        if 'countdown' not in self.database:
            self.database['countdown'] = "enabled"
        if self.user_params[0].lower() == "disable":
            self.database['countdown'] = "disabled"
        elif self.user_params[0].lower() == "enable":
            self.database['countdown'] == "disabled"
        elif len(self.user_params) == 0 and self.database['countdown'] == "enabled":
            try:
                count = int(self.user_params[0])
                if count > 10:
                    response_text = "I'm too lazy to do that..."
                elif count <= 0:
                    response_text = "Lets do it again!"
                else:
                    response_text = "!countdown " + str(count - 1)
                mentions = None

            except ValueError:
                response_text = "You think you're soooo clever? Not anymore " + self.author.first_name + ", because I now have error catching!"
                mentions = None
        elif len(self.user_params) == 0:
            response_text = "@" + self.author.first_name + "Countdown is now " + self.database['countdown']

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "NUMBER / DISABLE / ENABLE",
            "function": "Counts down recursively from NUMBER or ENABLE/DISABLES the countdown."
        }
