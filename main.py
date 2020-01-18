from fbchat import log, Client
import os
from fbchat import Message


# Subclass fbchat.Client and override required methods
class dentaku_bot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        if "!" in str(message_object.text)[0]:
            command = str(message_object.text).replace("!", "").split(" ")
            parameters = {
                "user": command[1:],
                "author_id": author_id,
                "message_object": message_object,
                "thread_id": thread_id,
                "thread_type": thread_type
            }
            command = command[0]
            try:
                module = __import__(command)
                new_command = getattr(module, command)
                instance = new_command(parameters, client=self)
            except ModuleNotFoundError:
                self.send(
                    Message(text="Command not found."),
                    thread_id=thread_id,
                    thread_type=thread_type,
                )
            except Exception as e:
                self.send(
                    Message(text="Error: " + str(e)),
                    thread_id=thread_id,
                    thread_type=thread_type,
                )

client = dentaku_bot(os.getenv('EMAIL'), os.getenv('PASSWORD'))
client.listen()