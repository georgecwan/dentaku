from pyshorteners import Shortener
from commands.command import Command
from fbchat import Message
from fbchat import Mention
import datetime
import dateutil.parser
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


class events(Command):

    def get_credentials(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        return creds

    def shorten_url(self, url):
        gat = os.environ['BITLY_GAT']
        shortener = Shortener('Bitly', bitly_token=gat)
        return format(shortener.short(url))

    def run(self):

        service = build('calendar', 'v3', credentials=self.get_credentials())

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=3, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])
        event_list = "*All upcoming events:*\n"

        if not events:
            event_list = "No upcoming events found."
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            event_list += event['summary'] + "\n" + dateutil.parser.parse(start).strftime(
                "%A, %b %-d at %-I:%M%p") + "\n" + self.shorten_url(event['htmlLink']) + "\n\n"

        response_text = "@" + self.author.first_name + "\n" + event_list
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "None",
            "function": "Find out what the next 3 vikingsDev events are."
        }
