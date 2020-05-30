from commands.command import Command
from fbchat import Message
from fbchat import Mention
import requests
import random
from bs4 import BeautifulSoup


class trivia(Command):

    def run(self):
        mentions = None
        commands = ["easy", "medium", "hard", "multiple", "boolean", "1", "2", "3", "4", "5", "6", "7","8",
                    "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
                    "24"]
        admins = ["George Wan"]
        if 'triviaAnswer' not in self.thread_data:
            self.thread_data['triviaAnswer'] = "n/a"
        if 'triviaPoints' not in self.thread_data:
            # Remove the try except after !trivia has been run on all Dentaku Instances
            try:
                self.thread_data['triviaPoints'] = self.thread_data['trivia']
            except:
                self.thread_data['triviaPoints'] = {}
        if len(self.user_params) > 0 and self.user_params[0].lower() == "reset":
            if self.author.name in admins:
                # Resets trivia ranking
                self.thread_data['triviaPoints'] = {}
                response_text = "The trivia ranking has been reset."
            else:
                response_text = "You are not authorized to use this command."
        elif len(self.user_params) > 0 and self.user_params[0].lower()[:4] == "rank":
            # Prints trivia ranking
            if len(self.thread_data['triviaPoints']) > 0:
                response_text = "Trivia Ranking:"
                for id, count in sorted(self.thread_data['triviaPoints'].items(), key=lambda x: x[1], reverse=True):
                    response_text += "\n{}: {}".format(self.getName(id), count)
            else:
                response_text = "Nobody has answered yet. Try sending !trivia to begin."
        elif len(self.user_params) > 0 and self.user_params[0].lower() == "help":
            response_text = '''Possible commands:
Easy: Easy question
Medium: Medium question
Hard: Hard question
Boolean: T/F question
Multiple: MC question

To see the category commands please send '!trivia categories'
Add the command after !trivia to use them.'''
        elif len(self.user_params) > 0 and self.user_params[0].lower()[:7] == "categor":
            response_text = '''Available Categories:
1: General Knowledge
2: Books
3: Film
4: Music
5: Theatre
6: Television
7: Video Games
8: Board Games
9: Science
10: Computers
11: Mathematics
12: Mythology
13: Sports
14: Geography
15: History
16: Politics
17: Art
18: Celebrities
19: Animals
20: Vehicles
21: Comics
22: Science: Gadgets
23: For Weebs
24: Cartoons/Animations

Add the number after !trivia to receive a question from the category.'''
        elif len(self.user_params) > 0 and self.thread_data['triviaAnswer'] != "n/a"\
                and self.user_params[0].lower() not in commands:
            # Receives the answer for the question
            mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
            response_text = "@" + self.author.first_name + " "
            if self.author_id not in self.thread_data['triviaPoints']:
                self.thread_data['triviaPoints'][self.author_id] = 0
            if self.thread_data['triviaAnswer'][0] == self.user_params[0].lower():
                response_text += "Congrats! You got it right!"
                self.thread_data['triviaPoints'][self.author_id] += self.thread_data['triviaValue']
            else:
                response_text += "Oof, the answer was actually " + self.thread_data['triviaAnswer']
                self.thread_data['triviaPoints'][self.author_id] -= 1
            response_text += "\nYou now have {} points.".format(self.thread_data['triviaPoints'][self.author_id])
            self.thread_data['triviaAnswer'] = "n/a"
            self.save_db()
        elif len(self.user_params) > 0 and self.user_params[0].lower() not in commands:
            return
        else:
            # Punishment for skipping questions
            if self.thread_data['triviaAnswer'] != "n/a":
                if self.author_id in self.thread_data['triviaPoints']:
                    self.thread_data['triviaPoints'][self.author_id] -= 1
                else:
                    self.thread_data['triviaPoints'][self.author_id] = -1
                prevAns = "The answer to the previous question was " + self.thread_data['triviaAnswer']
                self.client.send(
                    Message(text=prevAns),
                    thread_id=self.thread_id,
                    thread_type=self.thread_type
                )
            # Generates question to send
            url = "https://opentdb.com/api.php?amount=1"
            if len(self.user_params) > 0:
                for i in [x.lower() for x in self.user_params]:
                    if i in ["easy", "medium", "hard"]:
                        url += "&difficulty=" + i
                    elif i in ["multiple", "boolean"]:
                        url += "&type=" + i
                    elif i.isdigit() and 1 <= int(i) <= 24:
                        url += "&category={}".format(int(i) + 8)
            info = requests.get(url).json()['results'][0]
            info['question'] = str(BeautifulSoup(info['question'], features="html.parser"))
            info['correct_answer'] = str(BeautifulSoup(info['correct_answer'], features="html.parser"))
            for n in range(len(info['incorrect_answers'])):
                info['incorrect_answers'][n] = str(BeautifulSoup(info['incorrect_answers'][n], features="html.parser"))
            response_text = """Category: {}
Difficulty: {}
Q: {}""".format(info['category'], info['difficulty'], info['question'])
            if info['difficulty'] == "easy":
                self.thread_data['triviaValue'] = 2
            elif info['difficulty'] == "medium":
                self.thread_data['triviaValue'] = 3
            else:
                self.thread_data['triviaValue'] = 4
            if info['type'] == "boolean":
                self.thread_data['triviaValue'] -= 1
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
