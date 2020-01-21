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

## Dentaku API Documentation

[Check the Wiki for API Documentation](https://github.com/VikingsDev/Dentaku/wiki/API-Documentation)
