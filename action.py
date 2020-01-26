from fbchat import Client
import fbchat


class Action:

    def __init__(self, parameters=None, client: Client = None):
        self.database: dict = self.get(parameters, 'database')
        self.author_id: int = self.get(parameters, 'author_id')
        self.message_object: fbchat.Message = self.get(parameters, 'message_object')
        self.thread_id: int = self.get(parameters, 'thread_id')
        self.thread_type: fbchat.ThreadType = self.get(parameters, 'thread_type')

        self.documentation = {
            "parameters": "",
            "function": ""
        }

        self.client: fbchat.Client = client
        if client:
            self.author: fbchat.User = self.client.fetchUserInfo(self.author_id)[self.author_id]
            self.gdb = self.get(parameters, 'gdb')
            client.markAsDelivered(self.thread_id, self.message_object.uid)
            client.markAsRead(self.thread_id)
        self.define_documentation()

    def run(self):
        print("Running abstract command...")
        return

    def define_documentation(self):
        return

    def get(self, parameters, property):
        if parameters and property in parameters:
            return parameters[property]
        else:
            return None
