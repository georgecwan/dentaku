from commands.command import Command
from fbchat.models import *
from fbchat import Mention
from datetime import datetime

class ping(Command):

	def run(self):
		dt = datetime.utcnow().timestamp()*1000;

		self.client.send(
			Message(text = "Pong!"),
			thread_id = self.thread_id,
			thread_type = self.thread_type
		)
		ms = datetime.utcnow().timestamp()*1000;
		self.client.send(
			Message(text = str(int((int(ms) - int(dt)))) + "ms"),
			thread_id = self.thread_id,
			thread_type = self.thread_type
		)

	def define_documentation(self):
		self.documentation = {
			"parameters": "None",
			"function": "Check connection speed to bot"
		}