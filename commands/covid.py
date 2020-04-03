from commands.command import Command
from fbchat import Message
from fbchat import Mention
import pandas as pd
from datetime import date, timedelta
from bs4 import BeautifulSoup
import requests


class covid(Command):

    def run(self):
        country = ""
        if len(self.user_params) == 0:
            location = "British Columbia"
            response_text = self.csv_read(location, country)
        elif self.user_params[0].lower() == "global" or self.user_params[0].lower() == "world" or  self.user_params[0].lower() == "total":
            link = "https://www.worldometers.info/coronavirus/"
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = str(soup.find("div", class_="maincounter-number").find("span"))
            start = text.index(">") + 1
            end = text.index("<", 1)
            confirmed = text[start:end]
            text = str(soup.find_all("div", class_="maincounter-number")[1].find("span"))
            start = text.index(">") + 1
            end = text.index("<", 1)
            deaths = text[start:end]
            text = str(soup.find_all("div", class_="maincounter-number")[2].find("span"))
            start = text.index(">") + 1
            end = text.index("<", 1)
            recovered = text[start:end]
            response_text = ("@" + self.author.first_name + " Current global COVID-19 numbers:" + "\nConfirmed: " +
                             str(confirmed) + "\nDeaths: " + str(deaths) + "\nRecovered: " + str(recovered))
        else:
            location = " ".join(self.user_params)
            if "," in location:
                loclist = location.split(",")
                location = self.location_correct(loclist[0].strip())
                country = self.location_correct(loclist[1].strip())
            else:
                location = self.location_correct(location)
            response_text = self.csv_read(location, country)

        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "LOCATION",
            "function": "Returns the current coronavirus numbers for LOCATION. Global numbers are live, local numbers "
                        "update 5PM everyday. "
        }

    def csv_read(self, location, country):
        yesterday = str(date.today() - timedelta(days=1))[5:] + "-" + str(date.today() - timedelta(days=1))[:4]
        now = str(date.today())[5:] + "-" + str(date.today())[:4]
        try:
            url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data" \
                  "/csse_covid_19_daily_reports/{}.csv".format(now)
            try:
                response = pd.read_csv(url).drop(['FIPS', 'Admin2', 'Combined_Key', 'Lat', 'Long_'], axis=1)
            except:
                response = pd.read_csv(url)
        except:
            url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data" \
                  "/csse_covid_19_daily_reports/{}.csv".format(yesterday)
            try:
                response = pd.read_csv(url).drop(['FIPS', 'Admin2', 'Combined_Key', 'Lat', 'Long_'], axis=1)
            except:
                response = pd.read_csv(url)
        province_state = response.pop('Province_State').astype(str)
        response['Province_State'] = province_state
        try:
            countries = list(response['Country_Region'])
            regions = None
            rows = []
            tindex = 0
            if country == "":
                for i in countries:
                    if i.lower() == location.lower():
                        rows.append(tindex)
                    tindex += 1
                if len(rows) == 0:
                    regions = list(response['Province_State'])
                    tindex = 0
                    for i in regions:
                        if i.lower() == location.lower():
                            rows.append(tindex)
                        tindex += 1
                    loc = regions[rows[0]] + ", " + countries[rows[0]]
                else:
                    loc = countries[rows[0]]
            else:
                regions = list(response['Province_State'])
                for i in countries:
                    if i.lower() == country.lower() and regions[tindex].lower() == location.lower():
                        rows.append(tindex)
                    tindex += 1
                loc = regions[rows[0]] + ", " + countries[rows[0]]
            confirmed = 0
            deaths = 0
            recovered = 0
            for i in rows:
                confirmed += list(response.loc[i])[2]
                deaths += list(response.loc[i])[3]
                recovered += list(response.loc[i])[4]
            response_text = ("@" + self.author.first_name + " Current COVID-19 numbers for " + loc + ":" +
                             "\nConfirmed: " + str(confirmed) + "\nDeaths: " + str(deaths) + "\nRecovered: " + str(
                        recovered))
            if regions is not None:
                response_text += "\n\nRecovered numbers are not available for regions."
        except:
            response_text = "@" + self.author.first_name + " Location not found."
        return response_text

    def location_correct(self, location):
        locs = {
            "usa": "US",
            "united states": "US",
            "uk": "United Kingdom",
            "britain": "United Kingdom",
            "south korea": "Korea, South",
            "korea": "Korea, South",
            "vatican city": "Holy See",
            "vatican": "Holy See",
            "bosnia": "Bosnia and Herzegovina",
            "congo": "Congo (Kinshasa)",
            "drc": "Congo (Kinshasa)",
            "democratic republic of the congo": "Congo (Kinshasa)",
            "republic of the congo": "Congo (Brazzaville)",
            "ivory coast": "Cote d'Ivoire",
            "macedonia": "North Macedonia",
            "papua": "Papua New Guinea",
            "saint kitts": "Saint Kitts and Nevis",
            "saint vincent": "Saint Vincent and the Grenadines",
            "taiwan": "Taiwan*",
            "republic of china": "Taiwan*",
            "people's republic of china": "China",
            "mainland china": "China",
            "uae": "United Arab Emirates",
            "palestine": "West Bank and Gaza",
            "gaza": "West Bank and Gaza",
            "west bank": "West Bank and Gaza",
            "nz": "New Zealand",
            "washington dc": "District of Columbia",
            "dc": "District of Columbia",
            "bc": "British Columbia",
            "ny": "New York"
        }
        if location.lower() in locs:
            return locs[location.lower()]
        return location
