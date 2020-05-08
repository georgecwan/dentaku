from commands.command import Command
from fbchat import Message
import requests
from random import choice


class news(Command):

    def run(self):
        codes = {
            'argentina': "ar", 'australia': "au", 'austria': "at", 'belgium': "be", 'brazil': "br",
            'bulgaria': 'bg', 'canada': 'ca', 'china': "cn", 'colombia': "co", 'cuba': "cu",
            'czech republic': "cz", 'egypt': "eg", 'france': "fr", 'germany': "de", 'greece': "gr",
            'hong kong': "hk", 'hungary': "hu", 'india': "in", 'indonesia': "id", 'ireland': "ie",
            'israel': "il", 'italy': "it", 'japan': "jp", 'latvia': "lv", 'lithuania': "lt",
            'malaysia': "my", 'mexico': "mx", 'morocco': "ma", 'netherlands': "nl", 'new zealand': "nz",
            'nigeria': "ng", 'norway': "no", "phillipines": "ph", 'poland': "pl", 'portugal': "pt",
            'romania': "ro", 'russia': "ru", 'saudi arabia': "sa", 'serbia': "rs", 'singapore': "sg",
            'slovakia': "sk", 'slovenia': "si", 'south africa': "za", 'south korea': "kr",
            'sweden': "se", 'switzerland': "ch", 'taiwan': "tw", 'thailand': "th", 'turkey': "tr",
            'uae': "ae", 'united arab emirates': "ae", 'ukraine': "ua", 'united kingdom': "gb",
            'uk': "gb", 'united states': "us", 'venezuela': "ve"
        }
        args = " ".join(self.user_params)
        if len(self.user_params) == 0:
            url = "https://newsapi.org/v2/top-headlines?language=en&apiKey=620bb40ce29b4ba6877ca164e3b9f008"
        elif args.lower() == "list":
            url = None
        elif args.lower() in codes:
            url = "https://newsapi.org/v2/top-headlines?country={}&language=en&apiKey=620bb40ce29b4ba6877ca164e3b9f008"\
                .format(codes[args.lower()])
        else:
            url = "https://newsapi.org/v2/top-headlines?country={}&language=en&apiKey=620bb40ce29b4ba6877ca164e3b9f008"\
                .format(args.lower())
        if url is not None:
            try:
                json = requests.get(url).json()['articles']
                info = choice(json)
                response_text = "Here is your headline!\n"+info['title'] + "\n" + info['url']
            except:
                response_text = ("Unable to find specified country. Supported countries and "
                                 "their codes can be found at https://newsapi.org/sources. "
                                 "Alternatively, type !news list for a list of available "
                                 "countries. Sources may not be in English.")
        else:
            response_text = ""
            for i in codes:
                response_text += i + ", "
            response_text = response_text[:-3]

        self.client.send(
            Message(text=response_text),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "COUNTRY/LIST",
            "function": "Get a random recent headline."
        }
