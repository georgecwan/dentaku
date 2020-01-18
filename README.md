# Dentaku

Dentaku is VikingsDev's open source messenger bot.

## Setting up a development environment

1. Clone repository
`git clone https://github.com/VikingsDev/Dentaku.git`
2. Create virtual environment
`python -m venv venv`
3. Create export file
`touch export.sh`
4. Edit `export.sh` using a text editor, and add
```
export EMAIL=YOUR_FACEBOOK_ACCOUNT_EMAIL
export PASSWORD=YOUR_FACEBOOK_ACCOUNT_PASSWORD
```
5. Run the bot
`python main.py`

## Contribution guidelines

To add your own command, create a file named your command. For example, if I 
wanted to make a command called dog, and I wanted users to run it as `!dog`, I would create a file
called `dog.py`

Inside `dog.py`, start with this template:
<br>(replace all occurences of dog with your command name)
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

[fbchat Examples](https://fbchat.readthedocs.io/en/stable/examples.html)<br>
[fbchat Full Documentation](https://fbchat.readthedocs.io/en/stable/api.html)

## Command
All commands must inherit `command.py`<br>
Inheriting `command.py` gives you these variables:

### self.user_params <br>
  Parameters that the user passed in along with the command. <br>
  
  Example: "!dog p1 p2 p3" <br>
  user_params = ["p1","p2","p3"] <br>
  
### self.author_id <br>
ID of the person who sent this command.br>
### self.message_object <br>
The command's message object <br>
### self.thread_id <br>
ID of the chat this command was sent in <br>
### self.thread_type <br>
Type of the chat this command was sent in <br>
### self.client <br>
The Dentaku user account <br>
### self.author <br>
The object of the person who sent this message. <br>
