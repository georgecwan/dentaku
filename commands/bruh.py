import json

from fbchat import Message
from fbchat import Mention
import time
from commands.command import Command

statuses = ['confirmed', 'big']


class bruh(Command):

    def run(self):
        messenger_ref = self.gdb.collection(u'bruhs').document(u'messenger')

        try:
            int(self.user_params[0])
            command = "get"
        except ValueError:
            if not self.user_params[0]:
                return
            command = self.user_params[0]

        send_image = None

        if command == "get":
            if self.user_params[0] == "get":
                bruh_id = self.user_params[1]
            else:
                bruh_id = self.user_params[0]

            try:
                bruh_doc = messenger_ref.collection(u'bruhs').document(bruh_id).get().to_dict()
                status = bruh_doc['status']
            except TypeError:
                status = "Removed"

            if status == 'Removed':
                response_text = "@{}\nThis Bruh Moment does not exist.".format(self.author.first_name)
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
                        int(self.thread_id) not in messenger_ref.get().to_dict()['threads'][str(thread)]['shared']):
                    response_text = "@{}\nThis Bruh Moment is not accessible in this thread.".format(
                        self.author.first_name)
                else:
                    thread = self.client.fetchThreadInfo(thread)[thread]
                    thread = thread.name

                    time_string = time.strftime('%Y-%m-%d %-I:%M %p', time.localtime(bruh_doc['time']))

                    if 'image' in bruh_doc and bruh_doc['image']:
                        response_text = ("@{}\n"
                                         "Bruh *#{}*\n"
                                         "Thread: *{}*\n"
                                         "Status: *{}*\n"
                                         "Time Bruhed: *{}*\n\n"
                                         "Triggered by *{}* with this message:\n"
                                         "{}\n"
                                         "This was the bruh moment, by *{}*:").format(self.author.first_name, bruh_id, thread, status, time_string,
                                                      author, trigger, bro,
                                                      bruh_moment)
                        send_image = bruh_moment
                    else:
                        response_text = ("@{}\n"
                                         "Bruh *#{}*\n"
                                         "Thread: *{}*\n"
                                         "Status: *{}*\n"
                                         "Time Bruhed: *{}*\n\n"
                                         "Triggered by *{}* with this message:\n"
                                         "{}\n"
                                         "This was the bruh moment, by *{}*:\n"
                                         "{}").format(self.author.first_name, bruh_id, thread, status, time_string,
                                                      author, trigger, bro,
                                                      bruh_moment)

        elif command == "remove":
            if len(self.user_params) == 2:
                bruh_id = self.user_params[1]
                bruh_ref = messenger_ref.collection(u'bruhs').document(bruh_id)
                try:
                    bruh_doc = bruh_ref.get().to_dict()
                    status = bruh_doc['status']
                except TypeError:
                    status = "Removed"
                thread = bruh_doc['thread']
                if thread != self.thread_id and (
                        int(self.thread_id) not in messenger_ref.get().to_dict()['threads'][str(thread)]['shared']):
                    response_text = "@{}\nThis Bruh Moment is not accessible in this thread.".format(
                        self.author.first_name)
                else:
                    if status == "Removed":
                        response_text = "@{}\nBruh #{} does not exist.".format(self.author.first_name, bruh_id)
                    else:
                        bruh_doc['status'] = bruh_doc['moment'] = bruh_doc['trigger'] = bruh_doc['bro'] = author = bruh_doc[
                            'author'] = bruh_doc['thread'] = "Removed"

                        bruh_ref.update(bruh_doc)
                        response_text = "@{}\nBruh #{} has been removed.".format(self.author.first_name, bruh_id)
            else:
                response_text = "@{}\n Missing ID in arguments. Try !bruh remove ID".format(
                    self.author.first_name)
        elif command == "edit":
            if len(self.user_params) < 3:
                response_text = "@{}\nMissing {} parameters. Must be in the form !bruh edit ID NEW_BRUH_MOMENT".format(
                    self.author.first_name, 3 - len(self.user_params))
            else:
                bruh_id = self.user_params[1]
                bruh_ref = messenger_ref.collection(u'bruhs').document(bruh_id)
                try:
                    bruh_doc = bruh_ref.get().to_dict()
                    status = bruh_doc['status']
                except TypeError:
                    status = "Removed"

                thread = bruh_doc['thread']
                if thread != self.thread_id and (
                        int(self.thread_id) not in messenger_ref.get().to_dict()['threads'][str(thread)]['shared']):
                    response_text = "@{}\nThis Bruh Moment is not accessible in this thread.".format(
                        self.author.first_name)
                else:
                    if status == "Removed":
                        response_text = "@{}\nBruh #{} does not exist.".format(self.author.first_name, bruh_id)
                    else:
                        bruh_doc['moment'] = " ".join(self.user_params[2:])
                        bruh_doc['image'] = False
                        bruh_ref.update(bruh_doc)
                        response_text = "@{}\nBruh #{} has been edited.".format(self.author.first_name, bruh_id)
        elif command == "editimg":
            if len(self.user_params) < 3:
                response_text = "@{}\nMissing {} parameters. Must be in the form !bruh edit ID NEW_BRUH_MOMENT".format(
                    self.author.first_name, 3 - len(self.user_params))
            else:
                bruh_id = self.user_params[1]
                bruh_ref = messenger_ref.collection(u'bruhs').document(bruh_id)
                try:
                    bruh_doc = bruh_ref.get().to_dict()
                    status = bruh_doc['status']
                except TypeError:
                    status = "Removed"

                thread = bruh_doc['thread']
                if thread != self.thread_id and (
                        int(self.thread_id) not in messenger_ref.get().to_dict()['threads'][str(thread)]['shared']):
                    response_text = "@{}\nThis Bruh Moment is not accessible in this thread.".format(
                        self.author.first_name)
                else:
                    if status == "Removed":
                        response_text = "@{}\nBruh #{} does not exist.".format(self.author.first_name, bruh_id)
                    else:
                        bruh_doc['moment'] = "".join(self.user_params[2])
                        bruh_doc['image'] = True
                        bruh_ref.update(bruh_doc)
                        response_text = "@{}\nBruh #{} has been edited.".format(self.author.first_name, bruh_id)
        else:
            response_text = "@{}\n Not a valid command. Use either !bruh ID, !bruh remove ID, or !bruh edit ID TEXT".format(self.author.first_name)
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )
        if send_image:
            self.client.sendRemoteImage(
                send_image,
                thread_id=self.thread_id,
                thread_type=self.thread_type,
            )

    def define_documentation(self):
        self.documentation = {
            "parameters": "command ID TEXT",
            "function": "Accesses, removes, edits bruhs in the Bruh database. Commands: remove, edit. `!bruh ID` to get "
                        "bruh #ID, `!bruh edit ID TEXT` to set moment to TEXT, `!bruh removes ID` bruh ID from the database. "
        }
