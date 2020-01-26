import json

with open("database.json", 'r') as outfile:
    database = json.load(outfile)

if 'testing' in database:
    if database['testing'] == 'y':
        database['testing'] = 'n'
    else:
        database['testing'] = 'y'
    print("Testing mode has been turned " + ('on' if database['testing'] == 'y' else 'off'))
else:
    print("Testing mode will restrict all bot interactions to direct messages, or ThreadType.USER.")
    database['testing'] = input("Turn on testing mode? (This decision will be saved). (y/n): ")

with open("database.json", 'w') as outfile:
    json.dump(database, outfile)

print("Your decision has been saved. database['testing'] = " + database['testing'])
