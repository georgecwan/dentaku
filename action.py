import json

from fbchat import Client
import fbchat
from fbchat import TypingStatus
import asyncio


class Action:

    def __init__(self, parameters=None, client: Client = None):
        self.database: dict = self.get(parameters, 'database')
        self.author_id: int = self.get(parameters, 'author_id')
        self.message_object: fbchat.Message = self.get(parameters, 'message_object')
        self.thread_id: int = self.get(parameters, 'thread_id')
        self.thread_type: fbchat.ThreadType = self.get(parameters, 'thread_type')
        self.trigger = self.get(parameters, 'trigger')
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
        if parameters:
            if 'memory' not in self.database:
                self.database['memory']: dict = {}
            self.memory = self.database['memory']
            if str(self.thread_id) not in self.memory: self.memory[str(self.thread_id)]: dict = {}
            self.memory = self.memory[str(self.thread_id)]
            if 'thread' not in self.memory: self.memory['thread']: dict = {}
            self.thread_data = self.memory['thread']
            if str(self.author_id) not in self.memory: self.memory[str(self.author_id)]: dict = {}
            self.memory = self.memory[str(self.author_id)]
        self.define_documentation()

    def process(self):
        self.run()
        self.client.setTypingStatus(
            TypingStatus.STOPPED, thread_id=self.thread_id, thread_type=self.thread_type
        )

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

    def save_db(self):
        with open("database.json", 'w') as outfile:
            json.dump(self.database, outfile)

    def getName(self, id):
        # Returns the full name of the user based on their ID
        return self.client.fetchUserInfo(id)[id].name
