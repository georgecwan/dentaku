from commands import react
from keywords.keyword import Keyword
from fbchat import Message, MessageReaction
from fbchat import Mention


def auto_not():
    if react.auto == "off":
        return "on"
    return "off"


class auto_react(Keyword):

    def find_reaction_emoji(self):
        msg = self.message_object.text.split()
        ed = react.react.emoji_dict
        for m in msg:
            if m in ed:
                emoji = ed[m]
                return MessageReaction(emoji)

    def run(self):
        if react.auto == "off":
            exit()
        reply_id = react.find_reply_id(self.message_object)
        self.client.reactToMessage(reply_id, self.find_reaction_emoji())
        # response_text = "@" + self.author.first_name + " successful!"
        # mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
        # self.client.send(
        #     Message(text=response_text, mentions=mentions),
        #     thread_id=self.thread_id,
        #     thread_type=self.thread_type
        # )

    def define_documentation(self):
        self.documentation = {
            "trigger": "Words that make a bot emotional.",
            "function": "Allows Dentaku to react automatically at trigger words."
                        + "\n\nTo turn auto_react {}, type `!react auto {}`".format(auto_not(), auto_not())
        }
