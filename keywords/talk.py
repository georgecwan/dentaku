from commands.command import Command
from fbchat import Message
import dialogflow
import os


class talk(Command):
    def run(self):
        msg = self.message_object.text
        DIALOGFLOW_PROJECT_ID = 'dentaku-fyaltw'
        DIALOGFLOW_LANGUAGE_CODE = 'en-US'
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'dentaku-dialogflow.json'
        SESSION_ID = self.thread_id
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
        text_input = dialogflow.types.TextInput(text=msg, language_code=DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        response_text = response.query_result.fulfillment_text
        if self.client.uid != self.author_id:
            self.client.send(
                Message(text=response_text, reply_to_id=self.message_object.uid),
                thread_id=self.thread_id,
                thread_type=self.thread_type
            )

    def define_documentation(self):
        self.documentation = {
            "trigger": "bot",
            "function": "Hello from bot."
        }
