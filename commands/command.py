from fbchat import Client
class Command:

    def __init__(self, parameters, client: Client):
        self.user_params = parameters['user']
        self.author_id = parameters['author_id']
        self.message_object = parameters['message_object']
        self.thread_id = parameters['thread_id']
        self.thread_type = parameters['thread_type']
        self.client = client
        self.author = self.client.fetchUserInfo(self.author_id)[self.author_id]
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
