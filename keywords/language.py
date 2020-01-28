from fbchat import Message
from fbchat import Mention
from keywords.keyword import Keyword


class language(Keyword):

    def run(self):
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
        self.client.send(
            Message(text="@" + self.author.first_name + "WATCH YOUR LANGUAGE", mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "trigger": "@&#^$*&]",
            "function": "Warns you to watch your language."
        }
