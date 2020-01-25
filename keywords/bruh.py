from fbchat import Message
from fbchat import Mention
from keywords.keyword import Keyword


statuses = ['confirmed', 'big']

class bruh(Keyword):

    def run(self):


        replied_to: Message = self.message_object.replied_to
        for s in statuses:
            if s in self.message_object.text:
                status = s
        if replied_to:
            bruh_moment = replied_to.text
            bro = replied_to.replied_to.author
        else:
            messages = self.client.fetchThreadMessages(thread_id=self.thread_id, limit=10)
            messages.reverse()
            for m, i in zip(messages, range(len(messages))):
                if self.message_object.uid == m.uid:
                    bruh_moment = messages[i - 1].text

        trigger = self.message_object.text

        messenger_ref = self.gdb.collection(u'bruhs').document(u'messenger')
        messenger_bruhs = messenger_ref.get().to_dict()['latest_id']

        bruh_doc = messenger_ref.collection(u'bruhs').document(str(messenger_bruhs + 1))
        bruh_doc.set({
            u'trigger': trigger,
            u'moment': bruh_moment,
            u'thread': self.thread_id,
            u'author': self.author_id
        })
        messenger_ref.update({u'latest_id': messenger_bruhs + 1})
        response_text = """
        @{} Thank you for your entry. Bruh #{} has been logged into the Bruh Database.
        """.format(self.author.first_name, messenger_bruhs + 1)
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "None",
            "function": "More information on the vikingsDev website!"
        }
