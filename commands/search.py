from commands.command import Command
from fbchat import Message
from fbchat import Mention
try: 
	import googlesearch
except ImportError:  
	print("No module named 'google' found") 


class search(Command):

	def run(self):
		length = len(self.user_params)
		index = 1;
		query = ""

		for i in self.user_params:
			query += i
			if index < length:
				index += 1
				query += " "

		j = ""

		for j in googlesearch.search(query, tld="ca", num=1, stop=1, pause=2): 
			print(j) 

		response_text = "Here is Google's top search! " + j
		
		self.client.send(
			Message(text=response_text),
			thread_id=self.thread_id,
			thread_type=self.thread_type
		)

	def define_documentation(self):
		self.documentation = {
			"parameters": "SEARCH_TERM / SEARCH TERMS",
			"function": "Searches Google and gives you the best result for your search"
		}