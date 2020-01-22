from command import Command
from fbchat import Message
from fbchat import Mention
from fbchat import Client
from fbchat import MessageReaction
from fbchat import FBchatException


class react(Command):

    def find_reply_id(self, message):
        message_id = str(message).split()
        for x in message_id:
            if x.startswith("reply_to_id="):
                x = x.replace("reply_to_id='", "")
                x = x.replace("',", "")
                return x

    def find_reaction_emoji(self):
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
        if len(self.user_params) == 0:
            return None
        elif len(self.user_params) == 1:
            emoji = self.user_params[0].strip()
            try:
                emoji = MessageReaction(emoji)
                return emoji
            except ValueError:
                if emoji == "<3":
                    return MessageReaction("❤")
                response_text = "@" + self.author.first_name + "\nSorry, you can't react with that."
                self.client.send(
                    Message(text=response_text, mentions=mentions),
                    thread_id=self.thread_id,
                    thread_type=self.thread_type
                )
                return None
        else:
            response_text = "@" + self.author.first_name + "\nPlease input only 1 emoji."
            self.client.send(
                Message(text=response_text, mentions=mentions),
                thread_id=self.thread_id,
                thread_type=self.thread_type
            )
            return None

    def run(self):
        m = self.message_object
        yay = self.find_reply_id(m)
        try:
            self.client.reactToMessage(yay, self.find_reaction_emoji())
        except FBchatException:
            mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
            self.client.send(
                Message(text="Please select a message to reply to before reacting.", mentions=mentions),
                thread_id=self.thread_id,
                thread_type=self.thread_type
            )

    def define_documentation(self):
        self.documentation = {
            "parameters": "REPLIED_MESSAGE, EMOJI",
            "function": "Reacts to a REPLIED_MESSAGE with the specified EMOJI."
        }
