import json
import sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from fbchat import log, Client
import os
from fbchat import Message
from fbchat.models import *
import traceback
from datetime import datetime
import time
from fbchat import ThreadType
import importlib

database = {}


# Subclass fbchat.Client and override required methods
class dentaku_bot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        global database
        if database['testing'].lower() == "y" and thread_type != ThreadType.USER:
            return
        if "!" in str(message_object.text)[0]:
            message = str(message_object.text).replace("!", "").split(" ")
            command_index = 1
            if message[0] == '':
                for each in message:
                    if each != '':
                        command = each
                        break
                    command_index += 1
            else:
                command = message[0]
            try:
                parameters = {
                    "user": message[command_index:],
                    "author_id": author_id,
                    "message_object": message_object,
                    "thread_id": thread_id,
                    "thread_type": thread_type,
                    "database": database,
                    "gdb": gdb
                }
                module = importlib.import_module(".." + command, "commands.subpkg")
                new_command = getattr(module, command)
                instance = new_command(parameters, client=self)
                instance.run()
            except ModuleNotFoundError:
                print(traceback.format_exc())
                self.send(
                    Message(text="Command not found."),
                    thread_id=thread_id,
                    thread_type=thread_type,
                )
            except Exception as e:
                self.send(
                    Message(text="Error: " + traceback.format_exc()),
                    thread_id=thread_id,
                    thread_type=thread_type,
                )
        else:
            for word in keywords.keys():
                if word in message_object.text:
                    parameters = {
                        "author_id": author_id,
                        "message_object": message_object,
                        "thread_id": thread_id,
                        "thread_type": thread_type,
                        "database": database,
                        "gdb":gdb
                    }
                    module = importlib.import_module(".." + keywords[word], "keywords.subpkg")
                    new_command = getattr(module, keywords[word])
                    instance = new_command(parameters, client=self)
                    instance.run()


def export_env():
    with open("export.sh", "r") as file_in:
        for line in file_in:
            if "\"" in line:
                os.environ[line.split("=")[0].split(" ")[1]] = line[line.find("\"") + 1:line.rfind("\"")]
            else:
                line = line.replace("export", "").replace(" ", "")
                line = line.split("=")
                os.environ[line[0]] = line[1]


export_env()
client = dentaku_bot(os.getenv('EMAIL'), os.getenv('PASSWORD'))

if os.path.exists("database.json"):
    with open("database.json", 'r') as file:
        try:
            database = json.load(file)
        except json.decoder.JSONDecodeError:
            print("JSON file is invalid. Repair or delete database.json.")
            sys.exit()
        if 'deployment' in database:
            database['deployment'] += 1
        else:
            database['deployment'] = 0
    with open('database.json', 'w') as file:
        json.dump(database, file)
else:
    database = {"deployment": 0, "subscription": []}
    with open('database.json', 'w') as file:
        json.dump(database, file)

if os.path.exists("keywords.json"):
    with open("keywords.json", 'r') as file:
        try:
            keywords = json.load(file)
        except json.decoder.JSONDecodeError:
            print("JSON file is invalid. Repair or delete keywords.json.")
else:
    keywords = {}
    with open('keywords.json', 'w') as file:
        json.dump(keywords, file)

if 'testing' not in database:
    print("Testing mode will restrict all bot interactions to direct messages, or ThreadType.USER.")
    database['testing'] = input("Turn on testing mode? (y/n)")
    if input("Save this decision? (y/n)").lower() == 'y':
        with open('database.json', 'w') as file:
            json.dump(database, file)
            print("Decision saved to database.json with the key 'testing'")
else:
    print("Testing mode is currently " + ("on" if database['testing'].lower() == 'y' else 'off'))
    print("Mode is saved in database.json")

for thread in database['subscription']:
    client.send(Message(
        text="[" + datetime.now().strftime("%Y-%m-%d %-I:%M %p") + "] Dentaku deployed just now. #" + str(
            database['deployment'])),
        thread_id=client.uid, thread_type=ThreadType.USER)

 # Use a service account
cred = credentials.Certificate('bruh-moment-860fc-e104b9f587f9.json')
firebase_admin.initialize_app(cred)

gdb = firestore.client()

client.listen()
