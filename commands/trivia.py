from commands.command import Command
from fbchat import Message
from fbchat import Mention
import requests
import random


class trivia(Command):

    def run(self):
        if 'trivia' not in self.database:
            self.database['trivia'] = "n/a"
        if self.database['trivia'] == "n/a" or len(self.user_params) == 0:
            url = "https://opentdb.com/api.php?amount=1"
            info = requests.get(url).json()['results'][0]
            response_text = """Category: {}
Difficulty: {}
Q: {}""".format(info['category'], info['difficulty'], info['question'])
            choices = [info['correct_answer']]
            for c in info['incorrect_answers']:
                choices.append(c)
            random.shuffle(choices)
            index = 0
            if info['type'] == "multiple":
                letters = ["A", "B", "C", "D"]
            else:
                letters = ["A", "B"]
            for let in letters:
                if choices[index] == info['correct_answer']:
                    answer = index
                choices[index] = let + ": " + choices[index]
                index += 1
            self.database['trivia'] = choices[answer]
            for c in choices:
                response_text += "\n"+c
            response_text += "\n\nTo answer, type !trivia followed by the letter of your choice."
            self.client.send(
                Message(text=response_text),
                thread_id=self.thread_id,
                thread_type=self.thread_type
            )
        else:
            mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
            response_text = "@" + self.author.first_name + " "
            if self.database['trivia'][0] == self.user_params[0].upper():
                response_text += "Congrats! You got it right!"
            else:
                response_text += "Oof, the answer was actually "+self.database['trivia']
            self.database['trivia'] = "n/a"

            self.client.send(
                Message(text=response_text, mentions=mentions),
                thread_id=self.thread_id,
                thread_type=self.thread_type
            )

    def define_documentation(self):
        self.documentation = {
            "parameters": "None/ANSWER",
            "function": "Asks a trivia question."
        }
