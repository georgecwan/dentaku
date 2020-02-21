from commands.command import Command
from fbchat import Message
from fbchat import Mention
from commands.events import events


class bitly(Command):
    def run(self):
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
        response_text = "@" + self.author.first_name + " Here is your link: \n"
        steal = events()
        if len(self.user_params) != 0:
            try:
                url = steal.shorten_url(self.user_params[0])
                response_text += url
            except:
                try:
                    url = steal.shorten_url("http://"+self.user_params[0])
                    response_text += url
                except:
                    response_text = "@" + self.author.first_name + " Could not find link to shorten"
        elif self.message_object.replied_to != None:
            try:
                url = steal.shorten_url(self.message_object.replied_to.text)
                response_text += url
            except:
                try:
                    url = steal.shorten_url("http://"+self.message_object.replied_to.text)
                    response_text += url
                except:
                    response_text = "@" + self.author.first_name + " Could not find link to shorten"
        else:
            response_text = "@" + self.author.first_name + " Could not find link to shorten"

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "LINK or REPLIED_MESSAGE",
            "function": "Returns a bitly for the LINK."
        }
