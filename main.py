import json

from fbchat import log, Client
import os
from fbchat import Message
from fbchat.models import *
import traceback
from datetime import datetime
import time


# Subclass fbchat.Client and override required methods
class dentaku_bot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
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
                    "thread_type": thread_type
                }
                module = __import__(command)
                new_command = getattr(module, command)
                instance = new_command(parameters, client=self)
                instance.run()
            except ModuleNotFoundError:
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
        database = json.load(file)
        threads = database['subscription']
        if 'deployment' in database:
            database['deployment'] += 1
        else:
            database['deployment'] = 0
    with open('database.json','w') as file:
        json.dump(database, file)
else:
    database = {"deployment":0, "subscription":[]}
    with open('database.json','w') as file:
        json.dump(database, file)
for thread in threads:
    client.send(Message(
        text="[" + datetime.now().strftime("%Y-%m-%d %-I:%M %p") + "] Dentaku deployed just now. #" + str(database['deployment'])),
                thread_id=client.uid, thread_type=ThreadType.USER)
client.listen()
