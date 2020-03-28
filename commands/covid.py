from commands.command import Command
from fbchat import Message
from fbchat import Mention
import pandas as pd
from datetime import date, timedelta


class covid(Command):

    def run(self):
        if len(self.user_params) == 0:
            location = "Canada"
        else:
            location = " ".join(self.user_params)
            location = self.location_correct(location)
        yesterday = str(date.today() - timedelta(days=1))[5:] + "-" + str(date.today() - timedelta(days=1))[:4]
        now = str(date.today())[5:] + "-" + str(date.today())[:4]
        try:
            url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}.csv".format(
                now)
            try:
                response = pd.read_csv(url).drop(['FIPS', 'Admin2', 'Combined_Key', 'Lat', 'Long_'], axis=1)
            except:
                response = pd.read_csv(url)
        except:
            url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}.csv".format(
                yesterday)
            try:
                response = pd.read_csv(url).drop(['FIPS', 'Admin2', 'Combined_Key', 'Lat', 'Long_'], axis=1)
            except:
                response = pd.read_csv(url)
        province_state = response.pop('Province_State')
        response['Province_State'] = province_state
        countries = list(response['Country_Region'])
        rows = []
        tindex = 0
        confirmed = 0
        deaths = 0
        recovered = 0
        for i in countries:
            if i.lower() == location.lower():
                rows.append(tindex)
            tindex += 1
        for i in rows:
            confirmed += list(response.loc[i])[2]
            deaths += list(response.loc[i])[3]
            recovered += list(response.loc[i])[4]
        try:
            response_text = ("@" + self.author.first_name + " Current COVID-19 numbers for " + countries[rows[0]] + ":" +
               "\nConfirmed: " + str(confirmed) + "\nDeaths: " + str(deaths) + "\nRecovered: " + str(recovered))
        except:
            response_text = "@" + self.author.first_name + " Location not found."
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "LOCATION",
            "function": "Returns the current coronavirus numbers for LOCATION."
        }

    def location_correct(location):
        if location.lower() == "usa" or location.lower() == "united states":
            return("US")
        elif location.lower() == "uk" or location.lower() == "britain":
            return("UK")
        elif location.lower() == "south korea" or location.lower() == "korea":
            return("Korea, South")
        elif location.lower() == "vatican city" or location.lower() == "vatican":
            return("Holy See")
        elif location.lower() == "bosnia":
            return("Bosnia and Herzegovina")
        elif location.lower() == "congo" or location.lower() == "drc" or location.lower() == "democratic republic of the congo":
            return("Congo (Kinshasa)")
        elif location.lower() == "republic of the congo":
            return("Congo (Brazzaville)")
        elif location.lower() == "ivory coast":
            return("Cote d'Ivoire")
        elif location.lower() == "macedonia":
            return("North Macedonia")
        elif location.lower() == "papua":
            return("Papua New Guinea")
        elif location.lower() == "saint kitts":
            return("Saint Kitts and Nevis")
        elif location.lower() == "saint vincent":
            return("Saint Vincent and the Grenadines")
        elif location.lower() == "taiwan":
            return("Taiwan*")
        elif location.lower() == "uae":
            return("United Arab Emirates")
        elif location.lower() == "palestine" or location.lower() == "gaza" or location.lower() == "west bank":
            return("West Bank and Gaza")
        elif location.lower() == "nz":
            return("New Zealand")
        return(location)