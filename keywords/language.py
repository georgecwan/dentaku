from fbchat import Message
from fbchat import Mention
from keywords.keyword import Keyword


class language(Keyword):

    def run(self):
        if self.client.uid != self.author_id:
            if 'swears' not in self.thread_data:
                self.thread_data['swears'] = {}
            swearDict = self.thread_data['swears']
            if self.author_id not in swearDict:
                swearDict[self.author_id] = 1
            else:
                swearDict[self.author_id] += 1

            response_text = "@{} WATCH YOUR LANGUAGE\nSwear Count: {}"\
                .format(self.author.first_name.upper(),swearDict[self.author_id])
            mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
            self.client.send(
                Message(text=response_text, mentions=mentions, reply_to_id=self.message_object.uid),
                thread_id=self.thread_id,
                thread_type=self.thread_type
            )

    def define_documentation(self):
        self.documentation = {
            "trigger": "@&#^$*&]",
            "function": "Warns you to watch your language."
        }
