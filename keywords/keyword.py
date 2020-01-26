from fbchat import Client
from action import Action


class Keyword(Action):

    def __init__(self, parameters=None, client: Client=None):
        Action.__init__(self, parameters, client)
        self.documentation = {
            "trigger": "",
            "function": ""
        }
