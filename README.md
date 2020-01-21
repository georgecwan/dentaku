# Dentaku

Dentaku is VikingsDev's open source messenger bot.

## Setting up a development environment

1. Clone the repository.
`git clone https://github.com/VikingsDev/Dentaku.git`
2. Create a virtual environment.
`python -m venv venv`
3. Create an export file.
`touch export.sh`
4. Edit `export.sh` using a text editor, and add
```
export EMAIL="YOUR_FACEBOOK_ACCOUNT_EMAIL"
export PASSWORD="YOUR_FACEBOOK_ACCOUNT_PASSWORD"
export BITLY_GAT="YOUR_BITLY_GENERIC_ACCESS_TOKEN"
```
Note: Replace the strings with your own information, but keep the quotation marks! <br>
Get your bit.ly [Generic Access Token](https://bitly.com/a/oauth_apps), which is required if you want to use commands with link shorteners. <br>
(Remember to hit save in the text editor before activating the variables!) <br>
5. Activate the variables and venv. <br>
`source export.sh` <br>
`source venv/bin/activate` <br>
6. Install the required packages. <br>
`pip install -r requirements.txt` <br>
7. Run the bot. <br>
`python main.py` <br>
You should see this:
```
Logging in [YOUR_FACEBOOK_ACCOUNT_EMAIL]...
Login of [YOU_FACEBOOK_ACCOUNT_EMAIL] successful.
Listening...
```
Keep Dentaku running and check your Messenger! You should have received a message from yourself, saying "Dentaku is online." Test the 'help' command by sending `!help` to the chat. <br>
Now you can make your own commands by following the guidelines below. :)


## Contribution guidelines

For a full, comphrehensive read on contribution, take a look at our [CONTRIBUTING.md](CONTRIBUTING.md)

To add your own command, create a file named your command. For example, if I 
wanted to make a command called dog, and I wanted users to run it as `!dog`, I would create a file
called `dog.py`

Inside `dog.py`, start with this template: <br>
(replace all occurrences of dog with your command name)
```
from command import Command
from fbchat import Message
from fbchat import Mention


class dog(Command):

    def run(self):
        response_text = "@" + self.author.first_name + " Hello world! This is a dog command."
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions= mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )
```

These links might be helpful:

[fbchat Examples](https://fbchat.readthedocs.io/en/stable/examples.html) <br>
[fbchat Full Documentation](https://fbchat.readthedocs.io/en/stable/api.html)

## command.py, the `Command` class
All commands must inherit `command.py` <br>
Inheriting `command.py` gives you these variables:
### self.user_params <br>
Parameters that the user passed in along with the command. <br>
<br>Example: "!dog p1 p2 p3" <br>
user_params = ["p1", "p2", "p3"] <br>
### self.author_id <br>
ID of the person who sent this command. <br>
### self.message_object <br>
The command's message object. <br>
<br>Type: [fbchat.Message](https://fbchat.readthedocs.io/en/stable/api.html#fbchat.Message)
### self.thread_id <br>
ID of the chat this command was sent in. <br>
### self.thread_type <br>
Type of the chat this command was sent in. <br>
<br>Type: [fbchat.ThreadType(enum)](https://fbchat.readthedocs.io/en/stable/api.html#fbchat.ThreadType)
### self.client <br>
The Dentaku user account. <br>
<br>Type: [fbchat.Client](https://fbchat.readthedocs.io/en/stable/api.html#client)
### self.author <br>
The object of the person who sent this message. <br>
<br>Type: [fbchat.User](https://fbchat.readthedocs.io/en/stable/api.html#fbchat.User)
