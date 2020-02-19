from commands.command import Command
from fbchat import Message
from fbchat import Mention


class countdown(Command):

    def run(self):
        if 'countdown' not in self.database:
            self.database['countdown'] = "enabled"
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
        if len(self.user_params) == 0:
            response_text = "@" + self.author.first_name + " Countdown is currently " + self.database['countdown']
        elif self.user_params[0].lower() == "off":
            self.database['countdown'] = "disabled"
            response_text = "@" + self.author.first_name + " Countdown is now " + self.database['countdown']
        elif self.user_params[0].lower() == "on":
            self.database['countdown'] = "enabled"
            response_text = "@" + self.author.first_name + " Countdown is now " + self.database['countdown']
        elif len(self.user_params) == 1 and self.database['countdown'] == "enabled":
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
        else:
            response_text = "Sorry, !countdown is currently disabled. Please type !countdown ON and try again."
            mentions = None

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "NUMBER / ON / OFF",
            "function": "Counts down recursively from NUMBER or turns the countdown ON/OFF."
        }
