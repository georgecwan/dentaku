from commands.command import Command
from fbchat import Message
from fbchat import Mention
import dialogflow
import os

class talk(Command):

    def run(self):
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
        response_text = "@" + self.author.first_name + " "
        if len(self.user_params) > 0:
            text = " ".join(self.user_params)
            DIALOGFLOW_PROJECT_ID = 'dentaku-fyaltw'
            DIALOGFLOW_LANGUAGE_CODE = 'en-US'
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'dentaku-dialogflow.json'
            SESSION_ID = self.thread_id
            session_client = dialogflow.SessionsClient()
            session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
            text_input = dialogflow.types.TextInput(text=text, language_code=DIALOGFLOW_LANGUAGE_CODE)
            query_input = dialogflow.types.QueryInput(text=text_input)
            response = session_client.detect_intent(session=session, query_input=query_input)
            response_text += response.query_result.fulfillment_text
        else:
            response_text += "Please say something"
        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "MESSAGE",
            "function": "Makes small talk."
        }
