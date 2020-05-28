from commands.command import Command
from fbchat import Message
from fbchat import Mention
import requests
import random
from bs4 import BeautifulSoup


class trivia(Command):

    def run(self):
        mentions = None
        if 'triviaAnswer' not in self.thread_data:
            self.thread_data['triviaAnswer'] = "n/a"
        if 'trivia' not in self.thread_data:
            self.thread_data['trivia'] = {}
        if len(self.user_params) > 0 and self.user_params[0].lower() == "reset":
            # Resets trivia ranking
            self.thread_data['trivia'] = {}
            response_text = "The trivia ranking has been reset."
        elif len(self.user_params) > 0 and self.user_params[0].lower()[:4] == "rank":
            # Prints trivia ranking
            if len(self.thread_data['trivia']) > 0:
                response_text = "Trivia Ranking:"
                for id, count in sorted(self.thread_data['trivia'].items(), key=lambda x: x[1], reverse=True):
                    response_text += "\n{}: {}".format(self.getName(id), count)
            else:
                response_text = "Nobody has answered yet. Try sending !trivia to begin."
        elif len(self.user_params) > 0 and self.user_params[0].lower() == "help":
            response_text = '''Possible commands:
Easy, Medium, Hard: Sets difficulty of the question.

Add the command after !trivia to use them.'''
        elif len(self.user_params) > 0 and self.thread_data['triviaAnswer'] != "n/a":
            # Receives the answer for the question
            mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
            response_text = "@" + self.author.first_name + " "
            if self.author_id not in self.thread_data['trivia']:
                self.thread_data['trivia'][self.author_id] = 0
            if self.thread_data['triviaAnswer'][0] == self.user_params[0].lower():
                response_text += "Congrats! You got it right!"
                self.thread_data['trivia'][self.author_id] += self.thread_data['triviaValue']
            else:
                response_text += "Oof, the answer was actually " + self.thread_data['triviaAnswer']
            response_text += "\nYou now have {} points.".format(self.thread_data['trivia'][self.author_id])
            self.thread_data['triviaAnswer'] = "n/a"
            self.save_db()
        else:
            # Generates question to send
            if len(self.user_params) > 0 and self.user_params[0].lower() in ["easy", "medium", "hard"]:
                url = "https://opentdb.com/api.php?amount=1&difficulty=" + self.user_params[0].lower()
            else:
                url = "https://opentdb.com/api.php?amount=1"
            info = requests.get(url).json()['results'][0]
            info['question'] = str(BeautifulSoup(info['question'], features="html.parser"))
            info['correct_answer'] = str(BeautifulSoup(info['correct_answer'], features="html.parser"))
            for n in range(len(info['incorrect_answers'])):
                info['incorrect_answers'][n] = str(BeautifulSoup(info['incorrect_answers'][n], features="html.parser"))
            response_text = """Category: {}
Difficulty: {}
Q: {}""".format(info['category'], info['difficulty'], info['question'])
            if info['difficulty'] == "easy":
                self.thread_data['triviaValue'] = 1
            elif info['difficulty'] == "medium":
                self.thread_data['triviaValue'] = 2
            else:
                self.thread_data['triviaValue'] = 3
            choices = [info['correct_answer']]
            for c in info['incorrect_answers']:
                choices.append(c)
            random.shuffle(choices)
            index = 0
            if info['type'] == "multiple":
                letters = ["a", "b", "c", "d"]
            else:
                letters = ["a", "b"]
            for let in letters:
                if choices[index] == info['correct_answer']:
                    answer = index
                choices[index] = let + ") " + choices[index]
                index += 1
            self.thread_data['triviaAnswer'] = choices[answer]
            for c in choices:
                response_text += "\n"+c
            response_text += "\n\nTo answer, type !trivia followed by the letter of your choice."
            response_text += "\nTo learn how to customize the question, type '!trivia help'"

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "None / ANSWER/ 'help' / [ranking/reset]",
            "function": "Asks a trivia question."
        }
