from commands.command import Command
from fbchat import Message
import requests
from bs4 import BeautifulSoup
import googlesearch


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

		if length > 0:
			for j in googlesearch.search(query, tld="ca", num=1, stop=1, pause=2):
				print(j)

		if j == "":
			query = ""
			# get message from a replied thread
			target = self.message_object.replied_to
			if target is not None:
				query = target.text
			if query != "":
				for j in googlesearch.search(query, tld="ca", num=1, stop=1, pause=2):
					print(j)

		if j == "":
			response_text = "Please input a search term"
		else:
			response = requests.get(j)
			soup = BeautifulSoup(response.text, 'html.parser')
			metas = soup.find_all('meta')
			title = ([meta.attrs['content'] for meta in metas if
				   'property' in meta.attrs and meta.attrs['property'] == 'og:title'])
			description = ([meta.attrs['content'] for meta in metas if
				   'property' in meta.attrs and meta.attrs['property'] == 'og:description'])
			response_text = "Here are Google's top searches for those terms!\n"
			if len(title) > 0:
				response_text = title[0] + "\n"
			if len(description) > 0:
				response_text += "Snippet: " + description[0] + "\n"

			response_text += "\n" + j
		
		self.client.send(
			Message(text=response_text),
			thread_id=self.thread_id,
			thread_type=self.thread_type
		)

	def define_documentation(self):
		self.documentation = {
			"parameters": "SEARCH_TERM / SEARCH TERMS / REPLY TO MESSAGE",
			"function": "Searches Google for PARAMETERS and gives you the top result for your search"
		}