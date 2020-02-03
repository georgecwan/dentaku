from commands.command import Command
from fbchat.models import *
from fbchat import Mention
from datetime import datetime

class ping(Command):

	def run(self):
		dt = datetime.utcnow().timestamp()*1000;
		msg = ""

		try:
			getms = int(self.user_params[0])
			msg = "Pong! " + str(int(dt) - getms) + "ms"
		except IndexError:
			millis = datetime.utcnow().timestamp()*1000;
			msg = "!ping " + str(int(millis))

		self.client.send(
			Message(text = msg),
			thread_id = self.thread_id,
			thread_type = self.thread_type
		)

	def define_documentation(self):
		self.documentation = {
			"parameters": "None",
			"function": "Check connection speed to bot"
		}