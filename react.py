from command import Command
from fbchat import Message, Mention, MessageReaction, FBchatException
from random import choice as choose
from random import seed, randint


def find_reply_id(message):
    message_id = str(message).split()
    for x in message_id:
        if x.startswith("reply_to_id="):
            x = x.replace("reply_to_id='", "")
            x = x.replace("',", "")
            return x


class react(Command):

    # dictionary for "string": "emoji"
    emoji_dict = {
        # heart react "❤"
        "<3": "❤", "heart": "❤",
        # love react "😍"
        "love": "😍", "heart_eyes": "😍",
        # laugh react "😆"
        "laugh": "😆", "lol": "😆", "lmao": "😆", "haha": "😆", ":)": "😆", "xD": "😆", "XD": "😆", "yay": "😆",
        # wow react "😮"
        "wow": "😮", "whoa": "😮", "woah": "😮", "wows": "😮", "wtf": "😮", ":O": "😮", "O:": "😮", "truck": "😮",
        # sad react "😢"
        "sad": "😢", "crying": "😢", "sadness": "😢", "cry": "😢", ":(": "😢", ";-;": "😢", "</3": "😢", "):": "😢",
        # angry react "😠"
        "angry": "😠", "angr": "😠", "ugh": "😠", ">:(": "😠", "mad": "😠", "):<": "😠",
        # thumbs up react "👍"
        "thumbs_up": "👍", "yes": "👍", "good": "👍", "nice": "👍", "like": "👍", "up": "👍", "okay": "👍", "ok": "👍", "k": "👍", "yea": "👍",
        # thumbs down react "👎"
        "thumbs_down": "👎", "no": "👎", "bad": "👎", "ew": "👎", "dislike": "👎", "down": "👎", "not_okay": "👎", "not_ok": "👎", "nah": "👎",
        # random emoji!
        "random": "run_random", "r": "run_random", "react": "run_random"
    }

    def find_reaction_emoji(self):
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
        if len(self.user_params) == 0:
            return None
        elif len(self.user_params) == 1:
            emoji = self.user_params[0].strip().replace(":", "")
            try:
                emoji = MessageReaction(emoji)
                return emoji
            except ValueError:
                try:
                    emoji = self.emoji_dict[emoji]
                    if emoji == "run_random":
                        emoji = choose(["❤", "😍", "😆", "😮", "😢", "😠", "👍", "👎"])
                    return MessageReaction(emoji)
                except KeyError:
                    response_text = "@{}\nSorry, you can't react with that.".format(self.author.first_name)
                    self.client.send(
                        Message(text=response_text, mentions=mentions),
                        thread_id=self.thread_id,
                        thread_type=self.thread_type
                    )
                    return "invalid"
        else:
            response_text = "@{}\nPlease input only 1 emoji.".format(self.author.first_name)
            self.client.send(
                Message(text=response_text, mentions=mentions),
                thread_id=self.thread_id,
                thread_type=self.thread_type
            )
            return "invalid"

    def run(self):
        seed(randint(0, 100))
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]
        m = self.message_object
        reply_id = find_reply_id(m)
        try:
            emoji = self.find_reaction_emoji()
            if emoji != "invalid":
                self.client.reactToMessage(reply_id, self.find_reaction_emoji())
        except FBchatException:
            response_text = "@{}\nPlease select a message to reply to before reacting.".format(self.author.first_name)
            self.client.send(
                Message(text=response_text, mentions=mentions),
                thread_id=self.thread_id,
                thread_type=self.thread_type
            )

    def define_documentation(self):
        self.documentation = {
            "parameters": "REPLIED_MESSAGE, EMOJI",
            "function": "Reacts to a REPLIED_MESSAGE with the specified EMOJI."
        }
