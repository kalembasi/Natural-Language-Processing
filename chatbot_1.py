#create simple chatbot which learns from user
#once responses saved into JSON, it able to response same input as saved instance

import json
import os

def chat_bot():
    # Check if database file exists, otherwise start with an empty dictionary
    if os.path.exists("database_1.json"):
        with open('database_1.json', 'r') as f:
            database = json.load(f)
    else:
        database = {}

    while True:
        user_input = input("User: ")

        # Check if input is in database
        if user_input in database:
            print("Bot: ", database[user_input])
        else:
            print("Bot: I don't know how to answer, give me an instance.")
            user_example = input("User: ")
            database[user_input] = user_example

            # Save updated database
            with open('database_1.json', 'w') as f:
                json.dump(database, f)

chat_bot()
