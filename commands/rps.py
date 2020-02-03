from commands.command import Command
from fbchat import Message
from fbchat import Mention
from enum import Enum, unique
import random


class hand(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3
    SCISSORS = 3
    R = 1
    P = 2
    S = 3

    def __getitem__(self, item):
        if item == "ROCK":
            return self.ROCK
        elif item == "PAPER":
            return self.PAPER
        elif item == "SCISSOR":
            return self.SCISSOR
        else:
            raise KeyError("No key found for " + item)


class rps(Command):

    def run(self):
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        if not self.user_params:
            response_text = "@{} To begin your game, type !rps rock or !rps scissors or !rps paper.".format(self.author.first_name)
            self.client.send(
                Message(text=response_text, mentions=mentions),
                thread_id=self.thread_id,
                thread_type=self.thread_type
            )
            return

        if 'round' not in self.memory:
            self.client.send(
                Message(text="@{} New round begun!".format(self.author.first_name),
                        mentions=mentions),
                thread_id=self.thread_id,
                thread_type=self.thread_type
            )
            self.memory['round'] = 1
        bot_choice = random.choice([hand.ROCK, hand.PAPER, hand.SCISSOR])
        try:
            user_choice = hand(int(self.user_params[0]))
        except:
            try:
                user_choice = hand[self.user_params[0].upper()]
            except:
                response_text = "@{} Invalid input.".format(
                    self.author.first_name)
                self.client.send(
                    Message(text=response_text, mentions=mentions),
                    thread_id=self.thread_id,
                    thread_type=self.thread_type
                )
                return

        if 'bot' not in self.memory: self.memory['bot'] = 0
        if 'user' not in self.memory: self.memory['user'] = 0

        if user_choice == bot_choice:
            win = -1
        elif hand.ROCK == user_choice:
            win = 1 if bot_choice != hand.PAPER else 0
        elif hand.PAPER == user_choice:
            win = 1 if bot_choice != hand.SCISSOR else 0
        elif hand.SCISSOR == user_choice:
            win = 1 if bot_choice != hand.ROCK else 0

        self.client.send(
            Message(text="@{} ".format(self.author.first_name) + bot_choice.name.lower().capitalize() + "!",
                    mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

        if win == 1:
            response_text = "@{} You win!".format(self.author.first_name)
            self.memory['user'] += 1
        elif win == 0:
            response_text = "@{} You lose!".format(self.author.first_name)
            self.memory['bot'] += 1
        else:
            response_text = "@{} A tie!".format(self.author.first_name)
        response_text += "\n({}/3)\nDentaku {} - {} {}".format(self.memory['round'], self.memory['bot'],
                                                               self.memory['user'], self.author.first_name)

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

        if self.memory['round'] == 3:
            if self.memory['user'] > self.memory['bot']:
                response_text = "\n@{} Game over. You win!".format(self.author.first_name)
            elif self.memory['user'] == self.memory['bot']:
                response_text = "\n@{} Game over. You tied to a bot.".format(self.author.first_name)
            else:
                response_text = "\n@{} Game over. You lose lol".format(self.author.first_name)

            self.client.send(
                Message(text=response_text, mentions=mentions),
                thread_id=self.thread_id,
                thread_type=self.thread_type
            )
            del self.memory['round']
            del self.memory['bot']
            del self.memory['user']
        else:
            self.memory['round'] += 1

    def define_documentation(self):
        self.documentation = {
            "parameters": "ROCK/PAPER/SCISSOR",
            "function": "Plays a best out of 3 game of rock, papers, scissors."
        }
