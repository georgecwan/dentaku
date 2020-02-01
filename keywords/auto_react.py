from commands import react
from keywords.keyword import Keyword
from fbchat import MessageReaction


class auto_react(Keyword):

    def auto_not(self):
        if self.database["auto"] == "off":
            return "on"
        return "off"

    def find_reaction_emoji(self):
        msg = self.message_object.text.split()
        ed = react.react.emoji_dict
        for m in msg:
            if m in ed:
                emoji = ed[m]
                return MessageReaction(emoji)

    def run(self):
        if self.database["auto"] == "off":
            exit()
        reply_id = react.find_reply_id(self.message_object)
        self.client.reactToMessage(reply_id, self.find_reaction_emoji())

    def define_documentation(self):
        self.documentation = {
            "trigger": "Words that make a bot emotional.",
            "function": "Allows Dentaku to react automatically at trigger words."
                        + "\n\nTo turn auto_react {}, type `!react auto {}`".format(self.auto_not(), self.auto_not())
        }
