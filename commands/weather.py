from commands.command import Command
from fbchat import Message
from fbchat import Mention
from urllib.request import urlopen
import json
import bs4
import requests
import time

url = "http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&APPID=6f68045e525e16f8232fb0e5f19987c4".format("Burnaby")
print(url)
jsonurl = urlopen(url)
info = json.loads(jsonurl.read())#['list'][0]
print(info)
print(info['city']['country'])
print(time.asctime( time.localtime(info['city']['sunset'])))

class weather(Command):

    def run(self):
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
        response_text = "@" + self.author.first_name
        if len(self.user_params) == 0:
            response_text += " Please enter a city"

        elif self.user_params[0].lower() != "help":
            try:
                url = "http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&APPID=6f68045e525e16f8232fb0e5f19987c4".format("%20".join(self.user_params))
                jsonurl = urlopen(url)
                info = json.loads(jsonurl.read())
                response_text += " Weather at "+ info['city']['name'] + ", " + info['city']['country'] +\
                    "\n Population: " + str(info['city']['population'])
                info = info['list'][0]
                response_text += "\nCurrent temperature: " + str(info['main']['temp']) + "ºC"
                response_text += "\n\nMore info at "
            except:
                response_text += "Check for yourself at "
            try:
                link = "https://www.theweathernetwork.com/ca/search?q="
                for i in self.user_params:
                    if i == "-t":
                        break
                    else:
                        link += i + "%20"
                webpage = requests.get(link)
                text = str(bs4.BeautifulSoup(webpage.text, 'html.parser').find("li", class_="result"))
                h = text.find("href")
                e = text[h:].find(">")
                r = text[h:h + e]
                link = "https://www.theweathernetwork.com" + r[6:-1]
                response_text += link
            except:
                response_text = "@" + self.author.first_name + " Dude is that even a place."
            response_text += " \nFor a full list of commands type !weather help"
        else:
            response_text += " Possible Commands to add after the city:\nsunset, sunrise"

        self.client.send(
            Message(text=response_text, mentions= mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "CITY, COUNTRY(OPTIONAL), INFORMATION(OPTIONAL)",
            "function": "Gives you the link to a place to get the weather of a CITY because George isn't smart enough to get it for you."
        }