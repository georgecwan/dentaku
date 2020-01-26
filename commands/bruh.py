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

            status = bruh_doc['status']
            if status == 'Removed':
                response_text = "@{}\nThis Bruh Moment no longer exists.".format(self.author.first_name)
            else:
                bruh_moment = bruh_doc['moment']
                bruh_moment = "> " + bruh_moment
                bruh_moment = bruh_moment.replace("\n", "\n> ")

                trigger = bruh_doc['trigger']

                trigger = "> " + trigger
                trigger = trigger.replace("\n", "\n> ")

                bro = bruh_doc['bro']
                bro = self.client.fetchUserInfo(bro)[bro].name

                author = bruh_doc['author']
                author = self.client.fetchUserInfo(author)[author].name

                thread = bruh_doc['thread']

                if thread != self.thread_id and (
                        self.thread_id not in messenger_ref.get().to_dict()['threads'][str(thread)]['shared']):
                    response_text = "@{}\nThis Bruh Moment is not accessible in this thread.".format(
                        self.author.first_name,
                        bruh_id, thread,
                        author, trigger, bro,
                        bruh_moment)
                else:
                    thread = self.client.fetchThreadInfo(thread)[thread]
                    thread = thread.name
                    response_text = ("@{}\n"
                                     "Bruh *#{}*\n"
                                     "Thread: *{}*\n"
                                     "Status: *{}*\n\n"
                                     "Triggered by *{}* with this message:\n"
                                     "{}\n"
                                     "This was the bruh moment, by *{}*:\n"
                                     "{}").format(self.author.first_name, bruh_id, thread, status, author, trigger, bro,
                                                  bruh_moment)

        elif command == "remove":
            bruh_id = self.user_params[1]
            bruh_ref = messenger_ref.collection(u'bruhs').document(bruh_id)
            bruh_doc = bruh_ref.get().to_dict()
            bruh_doc['status'] = bruh_doc['moment'] = bruh_doc['trigger'] = bruh_doc['bro'] = author = bruh_doc[
                'author'] = bruh_doc['thread'] = "Removed"

            bruh_ref.update(bruh_doc)
            response_text = "@{}\nBruh #{} has been removed.".format(self.author.first_name, bruh_id)
        elif command == "edit":
            if len(self.user_params) < 3:
                response_text = "@{}\nMissing {} parameters. Must be in the form !bruh edit ID NEW_BRUH_MOMENT".format(
                    self.author.first_name, 3 - len(self.user_params))
            else:
                bruh_id = self.user_params[1]
                bruh_ref = messenger_ref.collection(u'bruhs').document(bruh_id)
                bruh_doc = bruh_ref.get().to_dict()
                bruh_doc['moment'] = self.user_params[2]
                bruh_ref.update(bruh_doc)
                response_text = "@{}\nBruh #{} has been edited.".format(self.author.first_name,bruh_id)
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "command ID TEXT",
            "function": "Accesses, removes, edits bruhs in the Bruh database. Commands: remove, edit. !bruh ID to get bruh #ID, !bruh edit ID TEXT to set ID to moment to text, !bruh removes bruh ID from the database."
        }
