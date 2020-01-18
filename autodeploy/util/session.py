import json
import os

Session = {}

if os.path.exists("../session.json"):
    with open('../session.json') as json_file:
        Session = json.load(json_file)
else:
    f = open("../session.json", "w")
    f.write("{}")
    f.close()


def get(property):
    if property in Session:
        return Session[property]
    else:
        Session[property] = -1
        write()
        return -1

def write():
    f = open("../session.json", "w")
    f.write(json.dumps(Session))
    f.close()

def set(property, value):
    Session[property] = value
    write()