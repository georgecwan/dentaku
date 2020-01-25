from fbchat import Message
from fbchat import Mention
import fbchat
from commands.command import Command


statuses = ['confirmed', 'big']

class bruh(Command):

    def run(self):
        messenger_ref = self.gdb.collection(u'bruhs').document(u'messenger')

        try:
            int(self.user_params[0])
            command = "get"
        except ValueError:
            command = self.user_params[0]
        if command == "get":
            bruh_id = self.user_params[0]
            bruh_doc = messenger_ref.collection(u'bruhs').document(bruh_id).get().to_dict()
            bruh_moment = bruh_doc['moment']
            trigger = bruh_doc['trigger']

            author = bruh_doc['author']
            author = self.client.fetchUserInfo(author)[author]
            author = author['first_name'] + " " + author['last_name']

            thread = bruh_doc['thread']
            thread = self.client.fetchGroupInfo(thread)[thread]
            thread = thread.name
            response_text = """
            @{}
            Bruh #{}
            Reporter: @{}
            Group: {}
            
            {}
            """.format(self.author.first_name, bruh_id, author, thread, bruh_moment)
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
