from fbchat import Client
import fbchat

class Command:

    def __init__(self, parameters, client: Client):
        self.database: dict = parameters['database']
        self.user_params: list = parameters['user']
        self.author_id: int = parameters['author_id']
        self.message_object: fbchat.Message = parameters['message_object']
        self.thread_id: int = parameters['thread_id']
        self.thread_type: fbchat.ThreadType = parameters['thread_type']
        self.client: fbchat.Client = client
        self.author: fbchat.User = self.client.fetchUserInfo(self.author_id)[self.author_id]
        self.documentation = {
            "parameters": "",
            "function": ""
        }
        client.markAsDelivered(self.thread_id, self.message_object.uid)
        client.markAsRead(self.thread_id)
        self.define_documentation()

    def run(self):
        print("Running abstract command...")
        return

    def define_documentation(self):
        return
