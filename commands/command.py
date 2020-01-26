from fbchat import Client
import fbchat
from action import Action


class Command(Action):

    def __init__(self, parameters=None, client: Client = None):
        Action.__init__(self, parameters, client)
        self.user_params: list = self.get(parameters, 'user')
