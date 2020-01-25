from fbchat import Client
import fbchat
from action import Action


class Command(Action):

    def __init__(self, parameters, client: Client):
        Action.__init__(self, parameters, client)
        self.user_params: list = parameters['user']
