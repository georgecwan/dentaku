from fbchat import Message
from keywords.keyword import Keyword


class bruh(Keyword):

    def run(self):

        self.client.send(
            Message(text="WATCH YOUR LANGUAGE", mentions=none),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "trigger": "@&#^$*&]",
            "function": "Warns you to watch your language."
        }
