from commands.command import Command
from fbchat import Message
from fbchat import Mention
from urllib.request import urlopen
import json
import bs4
import requests
import time

url = "http://api.openweathermap.org/data/2.5/forecast?q=Vancouver&units=metric&APPID=6f68045e525e16f8232fb0e5f19987c4"
jsonurl = urlopen(url)
info = json.loads(jsonurl.read())
list = info['list'][0]
#print(list)


class weather(Command):

    def run(self):
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
        response_text = "@" + self.author.first_name
        if len(self.user_params) == 0:
            response_text += " Please enter a city"
        elif "show" in [i.lower() for i in self.user_params]:
            index = 0
            for i in self.user_params:
                if i.lower() == "show":
                    break
                index += 1
            try:
                url = "http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&APPID=6f68045e525e16f8232fb0e5f19987c4".format("%20".join(self.user_params[:index]))
                jsonurl = urlopen(url)
                info = json.loads(jsonurl.read())
                response_text += " " + info['city']['name'] + ", " + info['city']['country']
                command = self.user_params[index+1].lower()
                if command == "population":
                    response_text += "\nPopulation: " + str(info['city']['population'])
                elif command == "sunrise":
                    response_text += "\nSunrise: " + str(time.asctime( time.localtime(info['city']['sunrise'])))
                elif command == "sunset":
                    response_text += "\nSunset: " + str(time.asctime(time.localtime(info['city']['sunset'])))
                elif command == "forecast" or command == "forecasts":
                    count = 1
                    for i in info['list']:
                        response_text += "\n"+str(count)+": "+i['dt_txt'][5:-3]
                        count += 1
                elif command.isdigit() and int(command) <= 40 and int(command) >0:
                    list = info['list'][int(command)-1]
                    response_text += ("\nForecast for " + str(list['dt_txt']) +
                                    "\nForecasted condition: " + str(list['weather'][0]['description']) +
                                    "\nForecasted temperature: " + str(list['main']['temp']) + "ºC"
                                    "\nFeels like: " + str(list['main']['feels_like']) + "ºC"
                                    "\nMaximum temperature: " + str(list['main']['temp_max']) + "ºC"
                                    "\nMinimum temperature: " + str(list['main']['temp_min']) + "ºC")
                elif command.isdigit() and (int(command) <1 or int(command) >40):
                    response_text += "Please enter a valid forecast number."
            except:
                response_text += " No command found"
        elif self.user_params[0].lower() != "help":
            try:
                url = "http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&APPID=6f68045e525e16f8232fb0e5f19987c4".format("%20".join(self.user_params))
                jsonurl = urlopen(url)
                info = json.loads(jsonurl.read())
                response_text += " Weather at "+ info['city']['name'] + ", " + info['city']['country']
                list = info['list'][0]
                response_text += ("\nCurrent condition: " + str(list['weather'][0]['main']) +
                        "\nCurrent temperature: " + str(list['main']['temp']) + "ºC")

                response_text += "\n\nMore info at "
                # Remove this if anti-zucc is added
                time.sleep(1)
            except:
                response_text += "\nCheck for yourself at "
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
            response_text += " You may type \"show\" after the city followed by:\nforecast, population, sunset, sunrise, 1-40"

        self.client.send(
            Message(text=response_text, mentions= mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "CITY, COUNTRY(OPTIONAL), COMMAND(OPTIONAL)",
            "function": "Gives you current information about a CITY because George figured out how to get it for you after a month."
        }